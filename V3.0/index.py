from captura import Captura
from procesamiento import Procesamiento
from morfologia import Morfologia
from segmentacion import Segmentacion
from graficas import Graficas 


# etapa de captura 
captura = Captura('img/toma10.jpg')
img = captura.get_img()
captura.show_img(img) # muestra la imagen original


# etapa de procesamiento 
pre_procesamiento = Procesamiento(img)
placa_img = pre_procesamiento.placa()
# pre_procesamiento.show_placa()


morfologia = Morfologia(placa_img)

# morfologia de la imagen original

img_bw = morfologia.gray(img)
img_thresh = morfologia.thresh(img_bw)


# morfologia de la placa 

mor_img = morfologia.get_img()

cierre = morfologia.cierre(mor_img)
blur = morfologia.blur(cierre)
bw = morfologia.gray(cierre)
thresh = morfologia.thresh(bw)



# segmentacion de la imagen 
segmentacion = Segmentacion(thresh)
segmentacion.proccess()




# captura de graficas 

plot = Graficas(3,3)
plot.start()


plot.show_plot(img,1)
plot.show_plot(img_bw,2)
plot.show_plot(img_thresh,3)
plot.show_plot(placa_img,4)
plot.show_plot(cierre,5)
plot.show_plot(blur,6)
plot.show_plot(bw,7)
plot.show_plot(thresh,8)


plot.end_plotter()