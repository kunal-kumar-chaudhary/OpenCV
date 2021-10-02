import cv2 as cv  

img = cv.imread('bhai.jpg') # read the image
img = cv.resize(img, (500,400), interpolation=cv.INTER_AREA)
cv.imshow('image',img)

# converting our image into gray scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)

print(f"number of faces found is : {len(faces_rect)}")

# cv.imshow('faces_rect',faces_rect)

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y),(x+w,y+h), (0,255,0), thickness=2)

cv.imshow('detected image', img)

cv.waitKey(0)