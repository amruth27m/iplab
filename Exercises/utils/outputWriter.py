import os
import cv2

class OutputWriter:
    def __init__(self,dirname):
        self.outputDirName = os.path.join(os.path.abspath(os.path.curdir), str(dirname))

    def write(self,fileName,image):
        cv2.imwrite(self.outputDirName + '/' + fileName, image)
