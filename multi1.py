import cv2
import numpy as np
 
#Iniciamos la camara
captura = cv2.VideoCapture(0)
 
while(1):
     
    #Capturamos una imagen y la convertimos de RGB -> HSV
    _, imagen = captura.read()
    hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
 
    #Establecemos el rango de colores que vamos a detectar
    #En este caso de verde oscuro a verde-azulado y azul claro
    verde_bajos = np.array([49,50,50], dtype=np.uint8)
    verde_altos = np.array([80, 255, 255], dtype=np.uint8)
 
    #Se crea una mascara con los pixeles dentro del rango de azul y verde
    mask = cv2.inRange(hsv, verde_bajos, verde_altos)
 
    #Encontrar el area de los objetos que detecta la camara
    moments = cv2.moments(mask)
    area = moments['m00']
 
    #Descomentar para ver el area por pantalla
    #print area
    if(area > 2000000):
         
        #Buscamos el centro x, y del objeto
        x = int(moments['m10']/moments['m00'])
        y = int(moments['m01']/moments['m00'])
        #Mostramos sus coordenadas por pantalla
        print "x = ", x
        print "y = ", y
 
        #Dibujamos una marca en el centro del objeto
        
        cv2.rectangle(imagen, (x, y), (x+2, y+2),(0,0,255), 10)

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(imagen,'verde',(1,100), font, 4,(255,255,255),2)
        
     
    #Mostramos la imagen original con la marca del centro y
    #la mascara 
    cv2.imshow('mask', mask)
    cv2.imshow('Camara', imagen)
    tecla = cv2.waitKey(5) & 0xFF
    if tecla == 27:
        break
 
cv2.destroyAllWindows()