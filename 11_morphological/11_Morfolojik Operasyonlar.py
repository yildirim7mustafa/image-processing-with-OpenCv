import cv2
import matplotlib.pyplot as plt
import numpy as np

#resmi içe aktarma
img = cv2.imread("datai_team.jpg",0)
plt.figure(), plt.imshow(img,cmap="gray"), plt.axis("off"), plt.title("original")

#erozyon sınırları küçültme
kernel = np.ones((5,5), dtype = np.uint8)
result = cv2.erode(img, kernel, iterations = 1)
plt.figure(), plt.imshow(result,cmap="gray"), plt.axis("off"), plt.title("erode")

#genişleme dilation
result2 = cv2.dilate(img, kernel, iterations = 1)
plt.figure(), plt.imshow(result2,cmap="gray"), plt.axis("off"), plt.title("dilated")

#white noise
whiteNoise = np.random.randint(0,2, size = img.shape[:2])
whiteNoise = whiteNoise*255
plt.figure(), plt.imshow(whiteNoise,cmap="gray"), plt.axis("off"), plt.title("white noised")

noise_img = whiteNoise + img
plt.figure(), plt.imshow(noise_img,cmap="gray"), plt.axis("off"), plt.title("white noised image")

# açılma (beyaz gürültüyü azaltmak için uyguluyoruz ve genisletiyo)
opening = cv2.morphologyEx(noise_img.astype(np.float32), cv2.MORPH_OPEN,kernel)
plt.figure(), plt.imshow(opening,cmap="gray"), plt.axis("off"), plt.title("açılma ingilizcesini bilmiyorm")

#black noise
blackNoise = np.random.randint(0,2, size = img.shape[:2])
blackNoise = blackNoise*-255
plt.figure(), plt.imshow(blackNoise,cmap="gray"), plt.axis("off"), plt.title("black noised")

black_noise_img = blackNoise + img
black_noise_img[black_noise_img <= -245] = 0
plt.figure(), plt.imshow(black_noise_img,cmap="gray"), plt.axis("off"), plt.title("black noised img")

#kapatma önce genisletiyo sonra erozyon ile daraltıyo
closing = cv2.morphologyEx(black_noise_img.astype(np.float32), cv2.MORPH_CLOSE,kernel)
plt.figure(), plt.imshow(closing,cmap="gray"), plt.axis("off"), plt.title("kapatma ingilizcesini bilmiyorm")

#gradient yazı üzerindeki kenarları tespit ettik
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
plt.figure(), plt.imshow(gradient,cmap="gray"), plt.axis("off"), plt.title("gradient")













