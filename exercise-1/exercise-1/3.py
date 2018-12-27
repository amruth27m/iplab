import cv2
import numpy as np

image = np.zeros((64,64))
for x in range(0,64):
    for y in range(0,64):
        sqsum = abs(np.cos(np.sqrt(x*x + y*y)))
        image[x,y] = sqsum
cv2.imshow('test',image)
cv2.waitKey()