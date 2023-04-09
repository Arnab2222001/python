import cv2 as cv
from cv2 import rectangle
import numpy as np

blank=np.zeros((500,500,3),dtype='uint8')
blank[200:300,200:300]=0,0,250
cv.rectangle(blank,(0,0),(40,1),(0,255,0),thickness=-1)
cv.imshow('blank',blank)
cv.waitKey(0)