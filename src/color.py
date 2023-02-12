import serial
import numpy as np
import cv2

# Serial communication
Serial = serial.Serial('COM4', 9600, timeout=1)
Serial.reset_input_buffer()

# Farve array
colors = ["RED", "GREEN", "BLUE", "YELLOW", "ORANGE", "BROWN"]

# Lav farve dicts:
colors_lower = {
    "RED":      [  0,   185,  126 ],
    "GREEN":    [ 31,    82,  77  ],
    "BLUE":     [ 98,   162,  44  ],
    "YELLOW":   [ 11,   105,  130 ],
    "ORANGE":   [  2,   142,  151 ],
    "BROWN":    [  0,   106,  53  ] 
}

colors_upper = {
    "RED":      [ 17,   205,  146 ],
    "GREEN":    [ 51,   122,  157 ],
    "BLUE":     [ 118,  202,  124 ],
    "YELLOW":   [ 31,   145,  210 ],
    "ORANGE":   [ 22,   172,  181 ],
    "BROWN":    [ 20,   146,  133 ]
}

colors_disp = {
    "RED":      (   97, 97, 248 ),
    "GREEN":    (  91, 216, 56  ),
    "BLUE":     ( 208, 129, 15  ),
    "YELLOW":   (   0, 217, 253 ),
    "ORANGE":   (  54, 148, 255 ),
    "BROWN":    ( 102, 102, 155 ),
}


# Få en sort og hvid farvemaske ud fra nedre og øvre grænseværdier
def makeMask(hsvFrame, color):
    color_lower = np.array(colors_lower[color], np.uint8)
    color_upper = np.array(colors_upper[color], np.uint8)
    mask = cv2.inRange(hsvFrame, color_lower, color_upper)
    return mask

# Brug farvemasken til at tjekke hvis et af områderne har et areal som er over 300 pixels.
def makeContour(mask, imageFrame, color):
    col = colors_disp[color]
    found_color = False
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            found_color = True
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y), (x + w, y + h), col, 2)
            cv2.putText(imageFrame, f"{color} color", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, col)

    return found_color, imageFrame

# Start webcam og initialiser dictionary som holder styr på hvor mange farver der er fundet
webcam = cv2.VideoCapture(0)
found = dict(zip( [color for color in colors], [0 for _ in range(6)] ))
# found = {
#     "RED":    0,
#     "GREEN":  0,
#     "BLUE":   0,
#     "YELLOW": 0,
#     "ORANGE": 0,
#     "BROWN":  0
# }

# Start main loop
print("Starting!")
FRAME_CHECK = 15
frame_counter = 0
lastSent = ""
while(True):
    
    # Få en frame fra webcammet og konverter den til HSV.
    _, imageFrame = webcam.read()
    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)
    
    # Loop igennem farverne
    for color in colors:
        # Få mask
        mask = makeMask(hsvFrame, color)
        # Få den modificerede (kosmetiske) imageFrame og få om farven blev fundet.
        found_color, imageFrame = makeContour(mask, imageFrame, color)
        
        # Hvis den blev fundet, gem det.
        found[color] += 1 if found_color else 0

    # Inkrementer frame tælleren
    frame_counter = (frame_counter + 1) % FRAME_CHECK 
    if frame_counter == 0: # Gå igennem følgende loop hver 15'ne frame
        highest = ("", 0) # Variabel til at gemme den farve der er mest af
        for (color, val) in found.items():
            if val > 7: # Tjek om farven blev fundet i over halvdelen af frames'ne. Hvis den er, tjek om den er der i flere frames end den anden som var fundet til at være der flest gange
                if val > highest[1]:
                    highest = (color, val)
            found[color] = 0
        # Tjek om der er fundet en højeste, og tjek at den ikke er den sidste sendte for at tage højde for serial communication
        if highest[0] != "" and highest[0] != lastSent:
            lastSent = highest[0]
            print(lastSent)
            Serial.write(bytes(highest[0], 'ascii')) # Encode som bytes og send over Serial
    cv2.imshow('recognition', imageFrame) # Vis image feed som viser det kameraet ser.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        webcam.release()
        break