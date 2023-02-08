import serial
import numpy as np
import cv2

# serial communication
Serial = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
Serial.reset_input_buffer()

# color array
colors = ["RED", "BLUE", "GREEN", "YELLOW", "ORANGE", "BROWN"]

# make color dicts:
colors_lower = {
    "RED":      [  0, 174, 119 ],
    "GREEN":    [ 58, 54,  79  ],
    "BLUE":     [ 94, 216, 78  ],
    "YELLOW":   [  8, 90,  142 ],
    "ORANGE":   [  0, 131, 150 ],
    "BROWN":    [  0, 113,  51 ],
}

colors_upper = {
    "RED":      [ 15, 214, 199 ],
    "GREEN":    [ 78,  94, 159 ],
    "BLUE":     [114, 255, 158 ],
    "YELLOW":   [ 28, 130, 222 ],
    "ORANGE":   [ 20, 171, 230 ],
    "BROWN":    [ 17, 153, 131 ]
}

# get black & white mask
def makeMask(hsvFrame, color):
    color_lower = np.array(colors_lower[color], np.uint8)
    color_upper = np.array(colors_upper[color], np.uint8)
    mask = cv2.inRange(hsvFrame, color_lower, color_upper)
    return mask

# use black and white mask to check if the areas of a specific mask is over 300.
def makeContour(mask):
    found = 0
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            found += 1

    return found

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

FRAME_CHECK = 10
frame_counter = 0
while(True):
    
    _, imageFrame = webcam.read()
    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)
    for color in colors:
        mask = makeMask(hsvFrame, color)
        found[color] = makeContour(mask)

    frame_counter = (frame_counter + 1) % FRAME_CHECK 
    if frame_counter == 0:
        for (color, val) in found.items():
            if val > 6:
                Serial.write(bytes(color, 'utf-8'))
                found[color] = 0
            
    if cv2.waitKey(1) & 0xFF == ord('q'):
        webcam.release()
        break