import cv2
import numpy as np

img=cv2.imread('saibaba.jpg',1)
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
ball = img[400:787 , 445:753]
img[0:368, 0:308] = ball
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()