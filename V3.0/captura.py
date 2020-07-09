import cv2 as ocv 

class Captura:
    
    def __init__(self, img):
        self.__img = img

    def get_img(self):
        return ocv.imread(self.__img)


    def set_img(self,value):
        self.__img = value


    def show_img(self,img):
        ocv.imshow('Output', img)
        self.__sample_img()

        
    def __sample_img(self):
        ocv.moveWindow('Image', 45, 5)
        ocv.waitKey(0)


