import cv2 as cv
# make gray the picture
img = cv.imread('C:/Users/ARNAB/OneDrive/Pictures/photo/nature.jpg')
cv.imshow('nature', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# blur the image
# the (7,7)is had to be a add
blur = cv.GaussianBlur(img, (7, 7,), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)
# edge cascede
canny = cv.Canny(img, 125, 175)
cv.imshow('canny edgs', canny)
# diateing the image
dilated = cv.dilate(img, (7, 7), iterations=3)
cv.imshow('dilated', dilated)
# eroding
eroded = cv.erode(img, (7, 7), iterations=3)
cv.imshow('eroded', eroded)
# rsize the image size
resize = cv.resize(img, (500, 250), interpolation=cv.INTER_CUBIC)
cv.imshow('resize', resize)
# cropping
cropped = img[50:200, 200:400]
cv.imshow('cropped', cropped)
cv.waitKey(0)
