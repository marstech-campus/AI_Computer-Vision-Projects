from facial_emotion_recognition import EmotionRecognition
import cv2
import urllib.request #to access url 
import numpy as np
import imutils


er = EmotionRecognition(device='cpu')
url='http://192.168.1.5:8080/shot.jpg'
while True:
    imgPath = urllib.request.urlopen(url)
    imgNp = np.array(bytearray(imgPath.read()), dtype=np.uint8)
    frame = cv2.imdecode(imgNp, -1)
    
    frame = er.recognise_emotion(frame, return_type='BGR')
    cv2.imshow('frame', frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
cam.release()

