
import cv2
import urllib.request
import numpy as np
import tensorflow
import keras
 
model = tensorflow.keras.models.load_model("b1.h5")
url='http://192.168.43.214/240x240.jpg'
cv2.namedWindow("Live Transmission", cv2.WINDOW_AUTOSIZE)


while True:
    img_resp=urllib.request.urlopen(url)
    imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
    img=cv2.imdecode(imgnp,-1)
    
    pothole = model.predict(img)
    
    
    for x,y,w,h in pothole:
         cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
    
    
    cv2.imshow("live transmission",img)
    key=cv2.waitKey(10)
    if key==ord('q'):
        break


cv2.destroyAllWindows()