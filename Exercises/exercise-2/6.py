import cv2
import numpy as np
from utils.outputWriter import OutputWriter

img1 = cv2.imread('resources/add.tif',cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('resources/add1.tif',cv2.IMREAD_GRAYSCALE)


addition = np.zeros(img2.shape)
subtraction = np.zeros(img2.shape)
multiplication = np.zeros(img1.shape)
division = np.zeros(img1.shape)
for x in range(0, img1.shape[0]):
    for y in range(0, img1.shape[1]):
        addition[x, y] = img1[x, y] + img2[x, y]
        subtraction[x,y] = img1[x,y] - img2[x,y]
        multiplication[x,y] = img1[x,y]*2
        division[x,y] = img1[x,y]*0
cv2.imshow('Addition', addition)
cv2.imshow('Subtraction',subtraction)
cv2.imshow('Multiplication',multiplication)
cv2.imshow('Division',division)
cv2.waitKey(0)
