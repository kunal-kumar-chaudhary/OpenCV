import cv2 as cv  
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('bhai.jpg')
img = cv.resize(img, (400,300), interpolation=cv.INTER_AREA)
cv.imshow('image', img)



# converting our image into gray scale image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# simple thresholding
threshold, thres = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('threshold', thres)

threshold, thres_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('threshold_inv', thres_inv)

# Adapting thresholding
adaptive_threshold = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,
cv.THRESH_BINARY, 11, 3)
cv.imshow("adaptive threshold",adaptive_threshold)

cv.waitKey(0)