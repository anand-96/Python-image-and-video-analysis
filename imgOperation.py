import cv2
import numpy as np

img1=cv2.imread('face5.jpg')
img2=cv2.imread('face6.jpg')

add=cv2.addWeighted(img1,1,img2,1,0)
cv2.imshow('add',add)
cv2.waitKey(0)
cv2.destroyAllWindows()