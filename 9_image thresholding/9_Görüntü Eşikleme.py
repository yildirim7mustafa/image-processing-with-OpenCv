import cv2
import matplotlib.pyplot as plt

#resmi içe aktarma
img = cv2.imread("img1.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.figure()
plt.imshow(img, cmap="gray")
plt.axis("off")
plt.show()

#eşikleme (threshold)  60 ile 255 arasındaki değerleri beyaz yapıyor. _ONV eklersek siyah ve beyazlar yer değişiyor
_, thresh_img = cv2.threshold(img, thresh = 60, maxval = 255, type = cv2.THRESH_BINARY_INV)

plt.figure()
plt.imshow(thresh_img, cmap="gray")
plt.axis("off")
plt.show()

#uyarlamalı eşik değer (adaptif threshhold)
#(resim,maxvalue,eşikleme algortiması yöntemi,eşikleme türü,bloksize,c)
thresh_img2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,8)

plt.figure()
plt.imshow(thresh_img2, cmap="gray")
plt.axis("off")
plt.show()
