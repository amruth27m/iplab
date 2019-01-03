import cv2

img = cv2.imread('resources/sample.tif',cv2.IMREAD_GRAYSCALE)
minimum_pixel_value, maximum_pixel_value = 255,0

for x in range(0,img.shape[0]):
    for y in range(0, img.shape[1]):
        if img[x,y] <= minimum_pixel_value:
            minimum_pixel_value = img[x,y]
        if img[x,y] >= maximum_pixel_value:
            maximum_pixel_value = img[x,y]
print("Minimum pixel value is %d" %minimum_pixel_value)
print("Maximum pixel value is %d" %maximum_pixel_value)
cv2.imshow('Test',img)
cv2.waitKey(0)
