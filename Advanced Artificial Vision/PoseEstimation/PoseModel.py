# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 18:22:53 2023

@author: CRISTIAN
"""

import cv2 #procesamiento de la imagen
import mediapipe as mp #pose estimacion
import time 


class poseDetector():
    
    def __init__(self, mode=False, upBody=False, smooth=True,
                 detectionCon = False, trackCon = 0.5):
        
        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        
        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode,self.upBody,self.smooth,
                                     self.detectionCon,self.trackCon)
    
    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        
        if self.results.pose_landmarks:
            if draw: 
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks,
                                           self.mpPose.POSE_CONNECTIONS)
        return img
    
    def findPosition(self, img, draw=True):
        lmList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                #print(id,lm)
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id,cx,cy])
                if draw:
                    cv2.circle(img, (cx,cy), 5, (255,0,0), cv2.FILLED)
            return lmList

def main():
    cap = cv2.VideoCapture('PoseVideos/video2.mp4')
    pTime = 0
    detector = poseDetector()

    while True:
        succes, img = cap.read()
        img = detector.findPose(img)
        lmList = detector.findPosition(img, draw=False)
        if len(lmList) != 0:
            print(lmList[10])
            cv2.circle(img, (lmList[10][1],lmList[10][2]), 15, (0,0,255), cv2.FILLED)

        
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

if __name__ == "__main__":
    main()








