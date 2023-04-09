import cv2 as cv
import numpy as np
img=cv.imread('C:/Users/ARNAB/OneDrive/Pictures/photo/nature.jpg')

cv.imshow('nature',img)
def translate(img,x,y):
    transmat = np.float32([[1,0,x],[0,1,y]])
    dimension=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transmat,dimension)
# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translated = translate(img, -100, -100)
cv.imshow('Translated', translated)
#rotation
def rotate(img,angle,rotpoint=None):
    

cv.waitKey(0)