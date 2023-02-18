# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 19:08:11 2023

@author: CRISTIAN
"""
import cv2
import time
import PoseModel as pm


cap = cv2.VideoCapture('PoseVideos/video1.mp4')
pTime = 0
detector = pm.poseDetector()

while True:
    succes, img = cap.read()
    img = detector.findPose(img)
    lmList = detector.findPosition(img, draw=False)
    
    if len(lmList) != 0:
        print(lmList[14])
        cv2.circle(img, (lmList[14][1],lmList[14][2]), 15, (0,0,255), cv2.FILLED)

    
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    
    cv2.putText(img, str(int(fps)), (100,100), cv2.FONT_HERSHEY_SIMPLEX, 3,
                (255,0,0), 3)
    
    im2 = cv2.resize(img, (1366, 720))
    cv2.imshow('Image', im2)
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Destroy all the windows
cv2.destroyAllWindows()