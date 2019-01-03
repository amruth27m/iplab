import cv2
import numpy as np
import  os
outputDir = os.path.join(os.path.abspath(os.path.curdir),'output/3/')

image = np.zeros((64,64))
for x in range(0,64):
    for y in range(0,64):
        sqsum = abs(np.cos(np.sqrt(x*x + y*y)))
        image[x,y] = sqsum
cv2.imshow('test',image)
cv2.imwrite(outputDir+ "orginal.jpg",image)
for x in range(0,64):
    for y in range(0,64):
        image[x,y] = image[x,y]*255
cv2.imwrite(outputDir+"processed.jpg",image)
cv2.waitKey()