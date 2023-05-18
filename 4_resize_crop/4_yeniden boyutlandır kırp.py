import cv2

#orj
img = cv2.imread("lenna.png")
print("Resim boyutu: ", img.shape)
cv2.imshow("Original", img)

#resize
imgResize = cv2.resize(img,(800,800))
print("Resized img shape", imgResize.shape)
cv2.imshow("Img Resize", imgResize)

#corp
imgCropped = img[:200,:300] # x ekseninde 0 dan 200 e , y ekseninde 0 dan 300 e 
print("Cropped img shape", imgCropped.shape)
cv2.imshow("Img cropped", imgCropped)


cv2.waitKey(0)

cv2.destroyAllWindows()