import cv2 as cv 
import numpy as np

img = cv.imread('bhai.jpg')
img = cv.resize(img, (400,300), interpolation=cv.INTER_AREA)
cv.imshow('image', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('blank', blank)
print(img.shape)
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('mask', mask)

masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow('masked', masked)

cv.waitKey(0)
