import pytesseract
#Libreria para Reconocerlos digitos de la imagen 
pytesseract.pytesseract.tesseract_cmd = r'E:\Users\Erick\AppData\Local\Tesseract-OCR\tesseract'

class Segmentacion():


    def __init__(self,img):
        self.__img = img
        self.__text = ''

    # devuelve los digitos de la placa en texto 
    def proccess(self):
        self.__text = pytesseract.image_to_string(self.__img, config='--psm 8')
        return (self.__text)

    # def print(self):
    #     self.proccess()
    #     return print(self.__text)
