import cv2 as ocv 
import numpy as np 

class Procesamiento:

    def __init__(self,img):
        self.__img = img
        self.__placa = []
    #Dibuja los bordes de la placa
    def bordes(self):
        bordes = ocv.Canny(self.__img, 150, 200)
        return ocv.dilate(bordes, None, iterations=1) 
    #   recorta la placa
    def contorno(self):
        bordes = ocv.Canny(self.__img, 150, 200)
        bordes = ocv.dilate(bordes, None, iterations=1) 
        contorno,_ = ocv.findContours(bordes, ocv.RETR_LIST, ocv.CHAIN_APPROX_SIMPLE)
        
        for c in contorno:
            x,y,w,h = ocv.boundingRect(c) # sacar  el largo y ancho y coordenadas posicion x y
            if len(self.__approx(c)) == 4 and self.__area(c) > 9000:

                if self.__ratio(w,h) > 1.5:
                    h2 = int(h/3)
                    w2 = w-10
                    self.__placa = self.__img[y+h2:y+h, x+8:x + w-8]
    # area de la placa
    def __area(self,c):
        return ocv.contourArea(c)
    
    # porcentaje aproximado del borde
    def __approx(self,c):
        epsilon = 0.09 * ocv.arcLength(c,True) # devuelve los porcentajes de luz
        return ocv.approxPolyDP(c, epsilon, True)
    # promedio entre el ancho y alto de placa
    def __ratio(self,w,h):
        return float(w)/h
    # almacena la placa 
    def placa(self):
        self.contorno()
        return self.__placa   
        
    #imprime placa original
    def show_placa(self):
        ocv.imshow('Placa', self.__placa)
        self.__sample_img()
    # crear la figura 
    def __sample_img(self):
        ocv.moveWindow('Out', 45, 5)
        ocv.waitKey(0)


