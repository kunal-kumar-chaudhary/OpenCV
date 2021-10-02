import cv2 as cv 
import numpy as np 



img = cv.imread('bhai.jpg')
img = cv.resize(img, (400,300), cv.INTER_AREA)
cv.imshow('image', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray) 

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('thresh', thresh)

canny = cv.Canny(img, 125, 175)
cv.imshow('canny', canny)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f"we found {len(contours)} contours")

cv.drawContours(blank, contours, -1, (0,0,255), 2)
cv.imshow('contour image', blank)

cv.waitKey(0)
