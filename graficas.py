
import matplotlib.pyplot as ptl

class Graficas:

    def __init__(self,x,y):
        self.__x = x
        self.__y = y 

    def start(self):
        return ptl.figure(1)
    

    def end_plotter(self):
        return ptl.show()


    def show_plot(self,img,pos):
        ptl.subplot(self.__x,self.__y, pos)
        return ptl.imshow(img)
