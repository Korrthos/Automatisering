# Python code for Multiple Color Detection
# https://www.geeksforgeeks.org/multiple-color-detection-in-real-time-using-python-opencv/


  
import numpy as np
import cv2

# color array
colors = ["red", "blue", "green", "blue", "orange", "brown"]

# make color dicts:
colors_lower = {
    "red":      [  0, 174, 119 ],
    "green":    [ 58, 54,  79  ],
    "blue":     [ 94, 216, 78  ],
    "yellow":   [  8, 90,  142 ],
    "orange":   [  0, 131, 150 ],
    "brown":    [  0, 113,  51 ],
}

colors_upper = {
    "red":      [ 15, 214, 199 ],
    "green":    [ 78,  94, 159 ],
    "blue":     [114, 255, 158 ],
    "yellow":   [ 28, 130, 222 ],
    "orange":   [ 20, 171, 230 ],
    "brown":    [ 17, 153, 131 ]
}

colors_disp = {
    "red":      (   97, 97, 248 ),
    "green":    (  91, 216, 56  ),
    "blue":     ( 208, 129, 15  ),
    "yellow":   (   0, 217, 253 ),
    "orange":   (  54, 148, 255 ),
    "brown":    ( 102, 102, 155 ),
}

def makeMask(hsvFrame, color):
    color_lower = np.array(colors_lower[color], np.uint8)
    color_upper = np.array(colors_upper[color], np.uint8)
    mask = cv2.inRange(hsvFrame, color_lower, color_upper)
    return mask

def morph(imageFrame, mask, kernal):
    mask = cv2.dilate(mask, kernal)
    result = cv2.bitwise_and(imageFrame, imageFrame, mask = mask)
    return mask, kernal

def makeContour(imageFrame, mask, color):
    col = colors_disp[color]
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y), (x + w, y + h), col, 2)
            cv2.putText(imageFrame, f"{color} color", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, col)
    return imageFrame



# Capturing video through webcam
webcam = cv2.VideoCapture(1)

# Start a while loop
while(True):
      
    # Reading the video from the
    # webcam in image frames
    _, imageFrame = webcam.read()
    # nimageFrame = cv2.resize(imageFrame, (0, 0), fx = 1, fy = 1);
    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)
    cv2.imshow('hsv', hsvFrame)
    for color in colors:
        mask = makeMask(hsvFrame, color)
        imageFrame = makeContour(imageFrame, masks[color], color)

    # Program Termination
    cv2.imshow("contours", imageFrame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        webcam.release()
        cv2.destroyAllWindows()
        break