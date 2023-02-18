# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 15:11:43 2023

@author: CRISTIAN
"""

import cv2 #procesamiento de la imagen
import mediapipe as mp #pose estimacion
import time 

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()


cap = cv2.VideoCapture('PoseVideos/video2.mp4')
pTime = 0

while True:
    succes, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    #print(results.pose_landmarks)
    
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            print(id,lm)
            cx, cy = int(lm.x * w), int(lm.y * h)
            cv2.circle(img, (cx,cy), 5, (255,0,0), cv2.FILLED)
    
    
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    
    cv2.putText(img, str(int(fps)), (70,50), cv2.FONT_HERSHEY_PLAIN, 3,
                (255,0,0), 3)
    
    im2 = cv2.resize(img, (1000, 720))
    cv2.imshow('Image', im2)
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  


