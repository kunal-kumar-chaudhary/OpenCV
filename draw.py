import cv2 as cv 
import numpy as np
img = cv.imread('pushing.png')
# cv.imshow('Cat', img)

blank = np.zeros((500,500,3), dtype=np.int8)
cv.imshow('Blank image', blank)

# 1. paint the image a certain color
blank[200:300, 300:400] = 0,25,0 # will produce green image
cv.imshow('Blank', blank)

# 2. draw a rectangle
cv.rectangle(blank, (0,0), (250,250), color=(0,255,0), thickness=cv.FILLED)
cv.imshow('rectangle', blank)

# 3. Draw a circle
cv.circle(blank, (250,250), 40, color=(0,0,255), thickness=cv.FILLED)
cv.imshow('CIRCLE', blank)

# 4. Draw a line
cv.line(blank, (0,0), (250,250), color=(255,255,255), thickness=3)
cv.imshow('line', blank)

# 5. write text on a image
cv.putText(blank, 'hello', (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('putting text', blank)

cv.waitKey(0)