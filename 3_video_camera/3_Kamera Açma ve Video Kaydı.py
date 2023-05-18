import cv2

#capture donanımımıza erişiyoruz
cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(width, height)

# video kaydet
writer = cv2.VideoWriter("video_kaydi2.mp4", cv2.VideoWriter_fourcc(*"DIVX"),20,(width,height)) #windows için çerçeveleri sıkıştırmak için kullanılıyor, fps , widht&height

while True:
    
    ret, frame = cap.read() #her bir cap.read()' i frame e aktarıyoruz. başarılı ise ret true 
    
    
    #save
    writer.write(frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"): break

cap.release()
writer.release()
cv2.destroyAllWindows()