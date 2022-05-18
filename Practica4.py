import cv2
import numpy as np


imagen1 = np.ones((600,500), np.uint8) #crear 
cv2.imwrite('negra.png',imagen1) #guardar 
Limagen = cv2.imread('negra.png') #leer 
Nimagen = Limagen.copy()

cv2.rectangle(Nimagen,(100,300),(290,200),(0,0,255),12)#dibujar
cv2.circle(Nimagen,(300,200),100,(0,255,255),5)  
cv2.putText(Nimagen, 'ABCD 19110265', (0,400),cv2.FONT_HERSHEY_COMPLEX, 1.5,(255,255,0),5)

#escribir texto
cv2.imshow('Imagen modificada', Nimagen) #mostrar 
cv2.imwrite('Nnegra.png',Nimagen) #guardar nueva imagen

cv2.waitKey(0)
cv2.destroyAllWindows()


im = cv2.imread("amonggreen.png")
r=cv2.selectROI(im)
imCrop = im[int(r[1]):int(r[1]+r[3]),int(r[0]): int(r[0]+r[2])]
cv2.imshow("image",imCrop)
cv2.waitKey(0)

#cv2.waitKey(0)
cv2.destroyAllWindows()
