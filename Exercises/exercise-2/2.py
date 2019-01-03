import cv2
import numpy as np
from utils.outputWriter import OutputWriter
import multiprocessing as mp

def oneDimensionConvolution(stream1, stream2):

    outputStream = []

    windowLength = len(stream2)
    for x in range(0,len(stream1)):
        sum = 0.0
        for y in range(0,len(stream2)):
            try:
                if(x - y + int(windowLength/2)) >=0:
                    sum += stream2[y]*stream1[x - y + int(windowLength/2)]
                    print("%f %f" %(stream2[y], stream1[x-y+ int(windowLength/2)]))
                else:
                    raise IndexError
            except IndexError:
                pass
        outputStream.append(sum)
        print("End")
    return outputStream

stream1 = [10,50,60,10,20,40,30]
stream2 = [1/3,1/3,1/3]
print(oneDimensionConvolution(stream1,stream2))
print(np.convolve(stream1,stream2))