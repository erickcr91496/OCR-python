import cv2
import numpy as np
import matplotlib.pyplot as ptl
import pytesseract


placa = []

# captura de la imagen
img = cv2.imread('img/toma1.jpg')

ptl.figure(2)
ptl.subplot(3, 3, 1)
ptl.imshow(img)

def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


def opening(image):
    kernel = np.ones((3, 3), np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)


# gray = get_grayscale(img) # imagen en escala de grises
# thresh = thresholding(gray)
# gray = cv2.blur(thresh, (3, 3)) # elimina el ruido de la imagen
bordes = cv2.Canny(img, 150, 200)  # deteccion de bordes con 2 umbrales
ptl.subplot(3, 3, 2)
ptl.imshow(bordes)
# Mejora de la imagen binaria bordes o resalte de bordes
bordes = cv2.dilate(bordes, None, iterations=1)
ptl.subplot(3, 3, 3)
ptl.imshow(bordes)

# Encontrando los contornos en la imagen blanco y negro
_,contorno,_ = cv2.findContours(bordes, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)


# dibujar todos los contornos encontrados
# cv2.drawContours(gray, contorno, -1, (0,255,0),2)


# encontrar la forma de rectangular la matriz
for c in contorno:
    # encontrar el area del rectangulo
    area = cv2.contourArea(c)

    # se saca el boundingBox
    x, y, w, h = cv2.boundingRect(c)

    # permite determinar los vertices del contorno
    epsilon = 0.09 * cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, epsilon, True)

    # se dibuja el contorno de la matricula con area mayor a 8000
    if len(approx) == 4 and area > 9000:
        aspect_ratio = float(w)/h

        # determinar el margen de error
        if aspect_ratio > 1.5:
            h2 = int(h/3)
            w2 = w-10
            placa = img[y+h2:y+h, x+8:x + w-8]
            

ptl.subplot(3, 3, 4)
ptl.imshow(placa)
kernel = np.ones((5, 5), np.uint8)
cierre = cv2.morphologyEx(placa, cv2.MORPH_CLOSE, kernel)
ptl.subplot(3, 3, 5)
ptl.imshow(cierre)
blur = cv2.medianBlur(cierre, 3)
bw = cv2.cvtColor(cierre, cv2.COLOR_BGR2GRAY)
ptl.subplot(3, 3, 6)
ptl.imshow(bw)
thresh = cv2.threshold(bw, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
# thresh = ~thresh
ptl.subplot(3, 3, 7)
ptl.imshow(thresh)
text = pytesseract.image_to_string(thresh, config='--psm 8')

print('text=', text)

cv2.imshow('Output', thresh)


cv2.moveWindow('Image', 45, 5)
cv2.waitKey(0)
ptl.show()