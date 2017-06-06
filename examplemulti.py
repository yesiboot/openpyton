import cv2
import numpy as np
 

captura = cv2.VideoCapture(0)

 
while(1):
     
    
    _, imagen = captura.read()
    hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV) 
    verde_bajos = np.array([49,50,50], dtype=np.uint8)
    
    #verde_altos = np.array([80, 255, 255], dtype=np.uint8)
    blue = np.array([130,255,255], dtype=np.uint8)
    mask = cv2.inRange(hsv, verde_bajos, blue)

    
    moments = cv2.moments(mask)
    area = moments['m00']
    if(area > 2000000):
        
        x = int(moments['m10']/moments['m00'])
        y = int(moments['m01']/moments['m00'])
        #z = int(moments['m01']/moments['m00'])
        
        print "x = ", x
        print "y = ", y
        #print "z = ", z
        cv2.rectangle(imagen, (x,y),(x+2, y+2), (0,0,255),10)
        
         

    cv2.imshow('mask', mask)
    cv2.imshow('Camara', imagen)
    tecla = cv2.waitKey(5) & 0xFF
    if tecla == 27:
        break
 
cv2.destroyAllWindows()