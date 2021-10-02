import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('bhai.jpg')
img = cv.resize(img, (400,300), cv.INTER_AREA)
cv.imshow('image', img)

plt.imshow(img) 

""" 
matplotlib displays image in RGB format but opencv displays image in BGR format.
"""
plt.show()

# we are going to deal with the color channels in this part
# BGR to greyscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('GRAR SCALED IMAGE', gray) 

# BGR TO HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv format', hsv)

# BGR TO LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab format', lab)   

# BGR TO RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb format', rgb)

# HSV TO BGR
hsv_bgr = cv.cvtColor(img, cv.COLOR_HSV2BGR)
cv.imshow('hsv-->>bgr', hsv_bgr)





cv.waitKey(0)  
