import numpy as np
from math import sqrt
import cv2

car_cascade = cv2.CascadeClassifier('cars.xml')

cap = cv2.VideoCapture(0)

while(True):
    ret, img = cap.read()
    img = cv2.flip(img, 0)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in cars:
        try:
            print (x, y, x+w, y+h)
            print (x+w)^2 + (y+h)^2
        except TypeError:
            print("Error")
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img,'Car',(x,y-10), font, 2,(255, 255, 255),1,cv2.LINE_AA)
            roi_gray = gray[y:y+h, x:x+h]
            roi_color = img[y:y+h, x:x+h]


    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.waitKey(0)
cv2.destroyAllWindows()
