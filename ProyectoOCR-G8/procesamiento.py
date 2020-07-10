import cv2 as ocv 
import numpy as np 
import pytesseract

class Procesamiento:

    def __init__(self,img):
        self.__img = img
        self.__placa = []

    def bordes(self):
        bordes = ocv.Canny(self.__img, 150, 200)
        return ocv.dilate(bordes, None, iterations=1) 

    def contorno(self):
        bordes = ocv.Canny(self.__img, 150, 200)
        bordes = ocv.dilate(bordes, None, iterations=1) 
        contorno,_ = ocv.findContours(bordes, ocv.RETR_LIST, ocv.CHAIN_APPROX_SIMPLE)
        
        for c in contorno:
            
            x,y,w,h = ocv.boundingRect(c)

            if len(self.__approx(c)) == 4 and self.__area(c) > 9000:

                if self.__ratio(w,h) > 1.5:
                    h2 = int(h/3)
                    w2 = w-10
                    self.__placa = self.__img[y+h2:y+h, x+8:x + w-8]
    
    def __area(self,c):
        return ocv.contourArea(c)
    

    def __approx(self,c):
        epsilon = 0.09 * ocv.arcLength(c,True)
        return ocv.approxPolyDP(c, epsilon, True)

    def __ratio(self,w,h):
        return float(w)/h


    def placa(self):
        self.contorno()
        return self.__placa
    

    def show_placa(self):
        ocv.imshow('Placa', self.__placa)
        self.__sample_img()


    def __sample_img(self):
        ocv.moveWindow('Out', 45, 5)
        ocv.waitKey(0)


