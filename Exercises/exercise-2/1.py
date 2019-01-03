import cv2
import numpy as np
from utils.outputWriter import OutputWriter

outWriter = OutputWriter('output/1')

img = cv2.imread('resources/sample.tif',cv2.IMREAD_GRAYSCALE)
pixel_sum = 0

for x in range(0,img.shape[0]):
    for y in range(0, img.shape[1]):
        pixel_sum += img[x,y]

mean_pixel_value = pixel_sum/(img.shape[0]*img.shape[1])
print("mean_pixel_intensity %f" %mean_pixel_value)

for x in range(0,img.shape[0]):
    for y in range(0,img.shape[1]):
        if(img[x,y]<=mean_pixel_value):
            img[x,y] = 0
        else:
            img[x,y] = 255

cv2.imshow("Binary",img)
outWriter.write("Binary_processed.jpg",img)
cv2.waitKey(0)