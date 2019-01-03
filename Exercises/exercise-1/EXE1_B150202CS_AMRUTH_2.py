import cv2
import numpy as np
import os

outputDir = os.path.join(os.path.abspath(os.path.curdir),'output/2/')

img = cv2.imread('resources/puppy_1024.jpg',cv2.IMREAD_GRAYSCALE)
orginal_dim = (1024,1024)
sizes = [(512,512),(256,256),(128,128),(64,64),(32,32),(16,16)]
for size in sizes:
    small = cv2.resize(img,size,interpolation=cv2.INTER_AREA)
    small = cv2.resize(small,orginal_dim)
    imageName = 'small' + str(size[0])
    cv2.imwrite(outputDir+str(size[0]) + '.jpg',small)
    cv2.imshow(imageName,small)
cv2.imshow("orginal",img)
cv2.waitKey(0)