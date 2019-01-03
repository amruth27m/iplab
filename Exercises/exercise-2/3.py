import cv2
import numpy as np
from utils.outputWriter import OutputWriter
import multiprocessing as mp

def oneDimensionConvolution(stream1, stream2):

    outputStream = np.zeros(stream1.shape)

    xwindowLength = stream2.shape[0]
    yWindowLength = stream2.shape[1]
    for i in range(0, stream1.shape[0]):
        for j in range(0, stream1.shape[1]):
            sum = 0.0
            for x in range(0, stream2.shape[0]):
                for y in range(0,stream2.shape[1]):
                    try:
                        if (i - x + int(xwindowLength)/2) >=0 and (j - y + int(yWindowLength)/2) >=0 :
                            # print("Herre")
                            sum += stream2[x,y]*stream1[(i-x + int(xwindowLength/2)),(j - y + int(yWindowLength))]
                        else:
                            raise IndexError
                    except IndexError:
                        pass
            print(sum)
    return outputStream

stream1 = [[1,2,3],[4,5,6],[7,8,9]]
stream1 = np.asarray(stream1)
stream2 = [[-1,-2,-1],[0,0,0],[1,2,1]]
stream2 = np.asarray(stream2)
print(oneDimensionConvolution(stream1,stream2))