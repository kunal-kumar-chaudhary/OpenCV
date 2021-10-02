import cv2 as cv
import numpy as np

img = cv.imread('bhai.jpg')
img = cv.resize(img, (500,400), interpolation=cv.INTER_AREA)
cv.imshow('image', img)

# averaging technique
average = cv.blur(img, (3,3))
"""
higher the kernel size, more will the picture be blurry.  
"""
cv.imshow('average', average)

# Gaussian blur  
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('gauss', gauss)

# median blur
median = cv.medianBlur(img, 3)
cv.imshow('median', median)

# Bilateral blur
bialateral = cv.bilateralFilter(img,5,15,15)
cv.imshow('Bilateral',bialateral)

cv.waitKey(0)
