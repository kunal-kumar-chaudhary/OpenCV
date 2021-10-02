# rescaling the image and videos
import cv2 as cv 

img = cv.imread('pushing.png')
cv.imshow('cat', img)


def RescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# reading videos
capture = cv.VideoCapture(r'C:\Users\ASUS\OneDrive - K.R. MANGALAM UNIVERSITY\Desktop\opencv\JupyterLab - Google Chrome 2021-09-20 00-07-53.mp4')

while True:
    # works for images, videos, live videos
    isTrue, frame = capture.read() 
    frame_resized = RescaleFrame(frame)
    cv.imshow('video', frame)
    cv.imshow('video resized', frame_resized)
    # breaking out of while loop so that loop doesnot run indefintely
    if cv.waitKey(20) & 0xFF==ord('d'):
        break


# rescaling image
resized_img = RescaleFrame(img, scale=0.2)
cv.imshow('resized cat image', resized_img)

# second method to rescale/resize the frames 
def changeRes(width, height):
    # it only works for live video
    capture.set(3,width)
    capture.set(4,height)

capture.release()
cv.destroyAllWindows()

