
import cv2 as cv
# in this stape i am import the image in the cv
#img= cv.imread('C:/Users/ARNAB/OneDrive/Pictures/photo/cat.jpg')
# in this stape i am diplaying the image
# cv.imshow('cat',img)
# in this stape i am initialize the key holding
# cv.waitKey(0)
#in this code we wre displaying the video file
capture = cv.VideoCapture(
    "E:/movies/Lehanga _ Jass Manak (Official Video) Satti Dhillo(1080P_HD).mp4")
while True:
    isTrue, frame = capture.read()
    if isTrue:
        cv.imshow('movies', frame)
        if cv.waitKey(20) & 0xFF == ord('d'):
            break
    else:
        break
capture.release()
cv.destroyAllwindows()
