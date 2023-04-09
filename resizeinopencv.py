
import cv2 as cv
from cv2 import resize
img = cv.imread('C:/Users/ARNAB/OneDrive/Pictures/photo/cat.jpg')
cv.imshow('cat', img)


#this mathod i work for the store images it not going to be work for the live images
def rescaleFrame(frame, scale=.2):
    width = int(frame.shape[1]*scale)
    hight = int(frame.shape[0]*scale)
    dimension = (width, hight)
    return cv .resize(frame, dimension, interpolation=cv.INTER_AREA)

#that the call for image resize
resize_image = rescaleFrame(img)

cv.imshow('img', resize_image)
# for the video we use the capture formate 
capture = cv.VideoCapture("E:/movies/Lehanga _ Jass Manak (Official Video) Satti Dhillo(1080P_HD).mp4")
while True:
    isTrue, frame = capture.read()
    #that the call for video resize
    frame_resize = rescaleFrame(frame)
    if isTrue:
        cv.imshow('movies', frame)
        cv.imshow('movies resize', frame)
        if cv.waitKey(5) & 0xFF == ord('d'):
            break
    else:
        break
capture.release()
cv.destroyAllwindows()


cv.waitKey(5)
