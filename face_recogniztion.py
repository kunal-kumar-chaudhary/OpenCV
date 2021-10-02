import numpy as np
import cv2 as cv 

haar_cascade = cv.CascadeClassifier('haar_face.xml')

# features = np.load('features.npy')
# label = np.load('label.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()

face_recognizer.read('face_trained.yml')

people = ['ben_afflek', 'elton_john', 'jerry_seinfeld', 'madonna', 'mindy_kaling']

img = cv.imread(r'D:\Downloads\archive (8)\val\ben_afflek\httpafilesbiographycomimageuploadcfillcssrgbdprgfacehqwMTENDgMDUODczNDcNTcjpg.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('person', gray)

faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]
    # now we will be predicting
    label, confidence = face_recognizer.predict(faces_roi)
    print(f"label = {people[label]} with a confidence of {confidence}")
    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0)
    , thickness=2)
    cv.rectangle(img,(x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('detect', img)

cv.waitKey(0)
 