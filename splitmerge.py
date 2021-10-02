import cv2 as cv
import numpy as np

img = cv.imread('bhai.jpg')
img = cv.resize(img, (500,400), interpolation=cv.INTER_AREA)
cv.imshow('image', img)

# splitting the image into respective color channels
b,g,r = cv.split(img)
cv.imshow('blue', b)
cv.imshow('green', g)
cv.imshow('red', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# let's merge these color channels together
merged = cv.merge([b,g,r])   
cv.imshow('merged', merged)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('blank image', blank)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('blue', blue)
cv.imshow('green', green)
cv.imshow('red', red)


cv.waitKey(0)