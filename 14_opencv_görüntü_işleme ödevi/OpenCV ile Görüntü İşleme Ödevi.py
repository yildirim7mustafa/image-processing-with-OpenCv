# opencv kütüphanesini içe aktaralım
import cv2

# matplotlib kütüphanesini içe aktaralım
import matplotlib.pyplot as plt

# resmi siyah beyaz olarak içe aktaralım
img = cv2.imread("odev1.jpg", 0)

# resmi çizdirelim
plt.figure(), plt.imshow(img, cmap= "gray"), plt.axis("off"),plt.title("original")

# resmin boyutuna bakalım
print(img.shape)

# resmi 4/5 oranında yeniden boyutlandıralım ve resmi çizdirelim
imgResize = cv2.resize(img, (454, 688))
print(imgResize.shape)
plt.figure(), plt.imshow(imgResize, cmap= "gray"), plt.axis("off"),plt.title("resized img")

# orijinal resme bir yazı ekleyelim mesela "kopek" ve resmi çizdirelim
imgWithText = cv2.putText(img, "Kopek",(420,130),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0))
plt.figure(), plt.imshow(imgWithText, cmap= "gray"), plt.axis("off"),plt.title("texted img")

# orijinal resmin 50 threshold değeri üzerindekileri beyaz yap altındakileri siyah yapalım, 
# binary threshold yöntemi kullanalım ve resmi çizdirelim
_, threshedImg = cv2.threshold(img, thresh = 50, maxval = 255, type = cv2.THRESH_BINARY)
plt.figure(), plt.imshow(threshedImg, cmap= "gray"), plt.axis("off"),plt.title("threshed img")

# orijinal resme gaussian bulanıklaştırma uygulayalım ve resmi çizdirelim
gaussianImg = cv2.GaussianBlur(img, ksize = (3,3), sigmaX = 7)
plt.figure(), plt.imshow(gaussianImg, cmap= "gray"), plt.axis("off"),plt.title("gaussian img")

# orijinal resme Laplacian  gradyan uygulayalım ve resmi çizdirelim
laplacian = cv2.Laplacian(img, ddepth = cv2.CV_16S)
plt.figure(), plt.imshow(laplacian, cmap = "gray"), plt.axis("off"), plt.title("Laplacian")

# orijinal resmin histogramını çizdirelim
imgHist = cv2.calcHist([img], channels = [0], mask= None, histSize = [256], ranges = [0,256])
print(imgHist.shape)
plt.figure(), plt.plot(imgHist)

















