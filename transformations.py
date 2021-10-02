import cv2 as cv 
import numpy as np 

img = cv.imread('bhai.jpg')
img = cv.resize(img, (500,400), interpolation=cv.INTER_AREA)
cv.imshow('image', img)

# Translation 
def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimesions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimesions)

# x --> left
# -x --> right 
# y --> up
# -y --> down

cv.imshow('translated image',translate(img,100,200))

# Rotation 
def rotation(img, angle, rotpoint=None):
    (height, width) = img.shape[:2]   

    if rotpoint is None:
        rotpoint = (width//2, height//2)  
    rotmat = cv.getRotationMatrix2D(rotpoint,angle,1.0)
    dimesions = (width,height)

    return cv.warpAffine(img, rotmat, dimesions)

rotated = rotation(img, 45)
cv.imshow('rotated', rotated)

# Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('resized', resized)

# flipping
flip = cv.flip(img, 0) # for horizontal flip, replace 0 with 1
cv.imshow('flip', flip)

# cropping
cropped = img[200:300, 400:500]
cv.imshow('cropped', cropped)

cv.waitKey(0)