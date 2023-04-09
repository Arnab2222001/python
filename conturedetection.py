import cv2 as cv
img=cv.imread('C:/Users/ARNAB/OneDrive/Pictures/photo/nature.jpg')
cv.imshow('img',img)
canny=cv.Canny(img,125,175)#threshold is use to reduce or increasethe intensity of an image,mat means the matrix;
cv.imshow('')
cv.waitKey(0)