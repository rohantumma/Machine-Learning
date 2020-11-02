import cv2, glob
gimg=glob.glob("L:\arm64\face detection\*.jpg")
detect=cv2.CascadeClassifier("L:\arm64\face detection\haarcascade_frontalface_default.xml")

for timg in gimg:
    img=cv2.cv2.imread(timg)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face=detect.detectMultiScale(gray, 1.25, 5)
    for(x,y,w,h) in face:
        cv2.imshow("detect multiple images",img)
    cv2.waitkey(2000)
    cv2.destoryAllWindows()