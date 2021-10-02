import cv2 as cv 
import matplotlib.pyplot as plt 
import numpy as np 

img = cv.imread('bhai.jpg')
img = cv.resize(img, (400,350), interpolation=cv.INTER_AREA)
cv.imshow('image', img)


blank = np.zeros(img.shape[:2], dtype='uint8')
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('mask', mask)



# we can compute histograms for both color and gray scale images
# we will start with computing for gray scale images

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

# mask = cv.bitwise_and(gray, gray, mask=circle)
# cv.imshow('mask', mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('masked', masked)

# grayscale histograms
# gray_hist = cv.calcHist([gray], [0], mask, [255], [0,256])
# plt.figure()
# plt.xlabel('bins')
# plt.ylabel('# of pixels')
# plt.xlim([0,256])
# plt.plot(gray_hist)
# plt.show()



# color image histogram

plt.figure()
plt.xlabel('bins')
plt.ylabel('# of pixels')

color=('b','g','r')
for i,col in enumerate(color):
    color_hist = cv.calcHist([img], [i], mask, [255], [0,256])
    plt.plot(color_hist, color=col)
    plt.xlim([0,256])

plt.show()


cv.waitKey(0)
