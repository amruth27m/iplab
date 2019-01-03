import cv2
import numpy as np

img = cv2.imread('resources/sample.tif',cv2.IMREAD_GRAYSCALE)
img = np.asarray(img, dtype="float")
maximum_intenstiy = np.amax(img)
print(maximum_intenstiy)

rangeValue = {
    0: [0, int(maximum_intenstiy/4)],
    0.25: [int(maximum_intenstiy/4), int(2*maximum_intenstiy/4)],
    0.5:  [int(2*maximum_intenstiy/4), int(3*maximum_intenstiy/4)],
    0.75:  [int(3*maximum_intenstiy/4), int(maximum_intenstiy)],
}

for x in range(0, img.shape[0]):
    for y in range(0, img.shape[1]):
        for key,value in rangeValue.items():
            if img[x,y] in range(value[0], value[1]):
                img[x,y] = key
                continue
        if img[x,y] == maximum_intenstiy:
            img[x,y] = 1

cv2.imshow('quantised',img)

#Increasing intensity proportionally for visibility
for x in range(0,img.shape[0]):
    for y in range(0,img.shape[1]):
        img[x,y] = img[x,y]*255

cv2.imshow('processed', img)
cv2.waitKey(0)
