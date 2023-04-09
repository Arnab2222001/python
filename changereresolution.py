import cv2 as cv
from cv2 import resize
#its only work for the live video
capture = cv.VideoCapture("E:/movies/Lehanga _ Jass Manak (Official Video) Satti Dhillo(1080P_HD).mp4")
def changeres(width,height):
 capture.set(3,width)
 capture.set(4,height)

