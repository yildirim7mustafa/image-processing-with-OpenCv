import cv2
import numpy as np

#resmi içe aktar
img = cv2.imread("kart.png")
cv2.imshow("Original",img)

#istenilen genislik ve yükseklik
width = 400 
height = 500 

pts1 = np.float32([[230,1],[1,472],[540,150],[338,617]]) #çevireceğimiz köşeler
pts2 = np.float32([[0,0],[0,height],[width,0],[width,height]]) #istenilen transform

matrix = cv2.getPerspectiveTransform(pts1,pts2)
print(matrix)

#donusturulumus resim
imgOutput = cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("Donusturulmus",imgOutput)

cv2.waitKey(0)
cv2.destroyAllWindows()