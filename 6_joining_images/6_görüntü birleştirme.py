import cv2
import numpy as np

#resmi içe aktar
img = cv2.imread("lenna.png")
cv2.imshow("Orj", img)

#birleştirelim yatay
hor = np.hstack((img,img))
cv2.imshow("Horizontal" , hor)

#birleştirelim dikey
ver = np.vstack((img,img))
cv2.imshow("Verticle" , ver)

cv2.waitKey(0)
cv2.destroyAllWindows()