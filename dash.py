import numpy as np
from math import sqrt
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')


cap = cv2.VideoCapture(0)

while(True):
    ret, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        print (x, y, x+w, y+h)
        hyp = int((x+w)^2 + (y+h)^2)
        print (x+w)^2 + (y+h)^2

        # # img = cv2.circle(img, (x+w/2,y+h/2), int(hyp*.8), (255, 0, 0), 2)
        # cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # # cv2.rectangle(img, (x, y-40), (x+w, y), (255, 0, 0), 2)
        # font = cv2.FONT_HERSHEY_SIMPLEX
        # cv2.putText(img,'Face',(x,y-10), font, 2,(255, 255, 255),1,cv2.LINE_AA)
        # roi_gray = gray[y:y+h, x:x+h]
        # roi_color = img[y:y+h, x:x+h]
        # eyes = eye_cascade.detectMultiScale(roi_gray)
        # for (ex, ey, ew, eh) in eyes:
        #     cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.waitKey(0)
cv2.destroyAllWindows()
