import cv2
import numpy as np
import os

image = np.zeros((64,64))
outputDir = os.path.join(os.path.abspath(os.path.curdir),'output/4/')

for x in range(0,64):
    for y in range(0,64):
        sqsum = abs(np.cos(np.sqrt(x*x + y*y)))
        if(sqsum<0.25):
            image[x,y] = 0
        if(sqsum>=0.25 and sqsum < 0.5):
            image[x,y] = 0.25
        if(sqsum>=0.5 and sqsum < 0.75):
            image[x,y] = 0.5
        if(sqsum>=0.75 and sqsum < 1):
            image[x,y] = 0.75
        if(sqsum == 1):
            image[x,y] = 1
cv2.imshow('test',image)
cv2.imwrite(outputDir + 'quantised.jpg',image)
cv2.waitKey()