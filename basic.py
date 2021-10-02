import cv2 as cv 
import numpy as np

img = cv.imread('bhai.jpg')
img = cv.resize(img, (400,300), interpolation=cv.INTER_AREA)
cv.imshow('image', img)

# converting to grayscale

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

# creating blur image 
"""
to increase the blur, we can increase the kernel size. but remember, kernel size can only
be odd.    
"""
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

# Edge cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('canny', canny)

# Dialating the image
dialated = cv.dilate(canny, (3,3), iterations=1)
cv.imshow('dialated',dialated)

# Eroding 
eroded = cv.erode(dialated, (3,3), iterations=1)
cv.imshow('eroded', eroded)

# Resizing
resize = cv.resize(img, (500,500))
cv.imshow('resize',resize)

# cropping
cropped = img[50:200, 200:400]
cv.imshow('cropped',cropped)

cv.waitKey(0)