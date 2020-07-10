from captura import Captura
from procesamiento import Procesamiento
from morfologia import Morfologia
from segmentacion import Segmentacion


# etapa de captura 
captura = Captura('img/toma1.jpg')
img = captura.get_img()
captura.show_img(img)


# etapa de procesamiento 
pre_procesamiento = Procesamiento(img)
placa_img = pre_procesamiento.placa()
# pre_procesamiento.show_placa()


# morfologia de la imagen 
morfologia = Morfologia(placa_img)
mor_img = morfologia.get_img()

cierre = morfologia.cierre(mor_img)
blur = morfologia.blur(cierre)
bw = morfologia.gray(cierre)
thresh = morfologia.thresh(bw)




# segmentacion de la imagen 
segmentacion = Segmentacion(thresh)
segmentacion.proccess()


morfologia.show_img(thresh)  #muestra la imagen thresh
# morfologia.show_img(bw)