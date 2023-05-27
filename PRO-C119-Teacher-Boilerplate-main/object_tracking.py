import cv2
import time
import math

video = cv2.VideoCapture("bb3.mp4")

#loadtracker
tracker=cv2.TrackerCSRT_create()
returned,image=video.read()
bbox=cv2.selectROI("tracking",image,False)
tracker.init(image,bbox)
def drawbox(image,bbox):
    x,y,w,h=int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle (image,(x,y),((x+w),(y+h)),(255,0,255),3,1)

while True:
    check,image = video.read()  
    sucess,bbox=tracker.update(image) 
    if sucess:
        drawbox(image,bbox)
    else:
        cv2.putText(image,"lost",(75,90),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,255),2)
    cv2.imshow("result",image)
            
    key = cv2.waitKey(25)

    if key == 32:
        print("Stopped!")
        break


video.release()
cv2.destroyALLwindows()



