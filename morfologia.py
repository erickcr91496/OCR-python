import cv2 as ocv 
import numpy as np 
# import pytesseract


class Morfologia():

    def __init__(self,img):
        self.__img = img

    def get_img(self):
        return self.__img

    def gray(self,img):
        return ocv.cvtColor(img, ocv.COLOR_BGR2GRAY)

    def cierre(self,img):
        kernel = np.ones((5,5), np.uint8)
        return ocv.morphologyEx(img, ocv.MORPH_CLOSE, kernel)

    # difuminar
    def blur(self,img):
        return ocv.medianBlur(img, 3)
    #umbralizacion

    def thresh(self,img):
        return ocv.threshold(img, 0, 255, ocv.THRESH_BINARY + ocv.THRESH_OTSU)[1]

    #
    def opening(self,img):
        kernel = np.ones((3,3),np.uint8)
        return ocv.morphologyEx(img, ocv.MORPH_OPEN, kernel)

    def show_img(self,img):
        ocv.imshow('Output', img)
        self.__sample_img()


    def __sample_img(self):
        ocv.moveWindow('Image', 45, 5)
        ocv.waitKey(0)
