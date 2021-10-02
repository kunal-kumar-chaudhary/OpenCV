import cv2 as cv 

# reading image
img = cv.imread('pushing.png')

cv.imshow('pushing', img) # it displays image in a new window

# reading videos
capture = cv.VideoCapture(r'C:\Users\ASUS\OneDrive - K.R. MANGALAM UNIVERSITY\Desktop\opencv\JupyterLab - Google Chrome 2021-09-20 00-07-53.mp4')

while True:
    isTrue, frame = capture.read() 
    cv.imshow('video', frame)
    # breaking out of while loop so that loop doesnot run indefintely
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

