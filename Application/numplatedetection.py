import cv2 as cv
import easyocr
import numpy as np
import matplotlib.pyplot as plt

def detect_numberplate(image):
    numberplatecacade=cv.CascadeClassifier('haarcascade_russian_plate_number.xml')

    img=cv.imread(image)
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

    noplates=numberplatecacade.detectMultiScale(gray,scaleFactor=1.2,minNeighbors = 5, minSize=(25,25))

    plate = None
    
    for (x,y,w,h) in noplates:
        cv.rectangle(gray,(x,y),(x+w,y+h),(255,0,0),2)
        plate = gray[y: y+h, x:x+w]


    # cv.imshow('plates',gray)
    # cv.imshow('plates',plate)

    # blur=cv.GaussianBlur(plate, (5, 5), 0)
    # edges = cv.Canny(plate, 50, 150)
        
    if plate is not None:
        cv.imwrite("detected_numberplate.jpg",plate)

        detection_threshold=0.7
        img="detected_numberplate.jpg"
        reader=easyocr.Reader(['en'],gpu=False)
        text_=reader.readtext(img)
        print(text_)
    else:
        print("Number plate not found")

    # cv.save(plate)
    # if cv.waitKey(0) & 0xFF == ord('q'):
    #     cv.destroyAllWindows()  

if __name__ == "main": 
    detect_numberplate("cropped_22.jpg")