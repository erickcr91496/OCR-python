# importar librerias 
from tkinter import *  
from tkinter import filedialog 
from PIL import ImageTk, Image



from captura import Captura
from procesamiento import Procesamiento
from morfologia import Morfologia
from segmentacion import Segmentacion
from graficas import Graficas 

# *********************************************

root = Tk() # instanciar la ventana principal 
root.title("Vision Artificial Grupo 5")
# root.geometry("680x500")
root.config(bg="green")

logo = PhotoImage(file="img/cisic.PNG")
# configuraciones del disenio del frame 
miFrame = Frame()   #crear el area de trabajo 
miFrame.pack()
miFrame.config(bg="red")
miFrame.config(width="750", height="800")
miFrame.config(bd=35)
miFrame.config(relief="groove")

# etiquetas label
# titulo = StringVar()
Label(miFrame, text="Reconocimiento de Placas Vehiculares", textvariable="",fg="blue",justify="center", font=("Comic Sans MS",12)).place(x=225,y=0)
Label(miFrame, text="Morocho Erik, Pai José & Vásconez Erick", fg="black", font=("",8)).place(x=10,y=20)
Label(miFrame,image=logo).place(x=420,y=620)


#FUNCIONES -------EVENTOS


def path_img():
   miFrame.archivo = filedialog.askopenfilename(title="Seleccione vehiculo", initialdir="E:/UTN\VIII SEMESTRE\Inteligencia Artificial\OCR\Software\Fotos de Vehiculos", filetypes=( ('JPEG / JFIF','*.jpg'), ('Portable Network Graphics','*.png'),      ('Windows Bitmap','*.bmp'),("All files", "*.*")))
   global path 
   path = miFrame.archivo


def open_data(): 
   global my_image
   path_img()
   path = miFrame.archivo
   img_resize = Image.open(miFrame.archivo)
   img =img_resize.resize((400,300))
   my_image = ImageTk.PhotoImage(img)
   # etapa de captura 
   # captura = Captura(path)
   # img = captura.get_img()

   # -------------
   my_image_label= Label(image=my_image,width="400", height="300").place(x=175,y=300)


def reconocer_placa1():
   # etapa de procesamiento 
   
   # etapa de captura 
   captura = Captura(path)
   img = captura.get_img()
   # captura.show_img(img) # muestra la imagen original


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
   #Imprimir en formulario

   var = StringVar();
   var.set(segmentacion.proccess());
   Label(miFrame, text= "Placa Reconocida: ", textvariable="",fg="black",justify="center", font=("Comic Sans MS",16)).place(x=200,y=200)
   Entry(miFrame, textvariable=var, fg="green", font=("Comic Sans MS",16)).place(x=400,y=200)
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




##BOTONES........************/////////////
btnOpenFile =Button(miFrame, text="Cargar Imagen del vehiculo", command= open_data, font=("Comic Sans MS",13), width="30", height="2", bg="#E9CA45", ).place(x=200,y=50)

btnReconocer =Button(miFrame, text="Reconocer Nro de placa", command=reconocer_placa1, font=("Comic Sans MS",13),width="30", height="2", bg="#0DED32").place(x=200,y=120)








root.mainloop()


