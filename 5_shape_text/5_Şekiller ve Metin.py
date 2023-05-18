import cv2
import numpy as np

#resim oluştur
img = np.zeros((512,512,3),np.uint8) # siyah resim 
print(img.shape)

cv2.imshow("Siyah", img)

# çizgi
cv2.line(img,(0,0),(512,512),(0,255,0),3) # (resim,başlangıc notası,bitiş noktası, renk(BGR), kalınlık)
cv2.imshow("Line", img)

# dikdörtgen
cv2.rectangle(img,(0,0),(256,256),(255,0,0),cv2.FILLED) #(resim,başlagıc,bitis,renk,istersek içini doldururuz)
cv2.imshow("Rectangle", img)

#cember
cv2.circle(img,(300,300),45,(0,0,255))
cv2.imshow("Circle", img)

#metin
cv2.putText(img,"Resim",(350,350),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255)) #(resim,başlangıc nok,font,kalınlı,renk)
cv2.imshow("Metin", img)


cv2.waitKey(0)
cv2.destroyAllWindows()