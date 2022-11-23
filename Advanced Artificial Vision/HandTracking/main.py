# -*- coding: utf-8 -*-
"""

@author: CRISTIAN
"""

import cv2
#import mediapipe as mp
import time
import HandTrackingModel as htm


def main():
    pTime = 0
    cTime = 0 
    vid = cv2.VideoCapture(0)
    detector = htm.handDetector()


    while(True):
         
        # Capture the video frame
        ret, img = vid.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img)
        if len(lmList) !=0:
            print(lmList[0])
        
        
        cTime = time.time()
        fps = 1 / (cTime-pTime)
        pTime = cTime
        
        cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
      
        # Display the resulting frame
        cv2.imshow('frame', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
              
    

if __name__ == "__main__":
    main()

    # Destroy all the windows
    cv2.destroyAllWindows()