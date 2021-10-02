import cv2 as cv 
import numpy as np   
import matplotlib.pyplot as plt 

img = cv.imread('bhai.jpg')
img = cv.resize(img, (400,300), interpolation=cv.INTER_AREA)
cv.imshow('image', img)


# converting our image into gray scale image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))                  
cv.imshow('laplace',lap)

# sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('combined sobel', combined_sobel)
cv.imshow('sobelx', sobelx)
cv.imshow('sobely', sobely)

# let's compare above two with canny edge detector
canny = cv.Canny(gray, 150, 175)
cv.imshow('canny', canny)



cv.waitKey(0)