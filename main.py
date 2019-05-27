# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 21:42:00 2019

@author: Manoj
"""
import numpy as np
import cv2
import time
from scipy import ndimage

def recordFrames():
    cap = cv2.VideoCapture("harry2.mp4")
 
    
    time.sleep(3)
 
    background=0
 
    for i in range(300):
        ret,background = cap.read()
 
        
        background = np.flip(background,axis=1)
        cv2.imwrite("background/back"+str(i)+".jpg",background )


def redColorDetection():
    
    cap = cv2.VideoCapture("harry2.mp4")
    background = cv2.imread("background/back25.jpg")
    
   
    k=1
    while True:
        ret, img = cap.read()
        if ret:
            
            print(ret)
            
            img  = np.flip(img,axis=1)
             
            
            hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
             
            
            lower_red = np.array([0,120,70])
            upper_red = np.array([10,255,255])
            mask1 = cv2.inRange(hsv, lower_red, upper_red)
             
           
            lower_red = np.array([170,120,70])
            upper_red = np.array([180,255,255])
            mask2 = cv2.inRange(hsv,lower_red,upper_red)
             
            
            mask1 = mask1+mask2
            cv2.imwrite("mask/mask"+str(k)+".jpg",mask1)
            
            
          
            
            mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3),np.uint8))
            mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3,3),np.uint8))
 
 
            
            mask2 = cv2.bitwise_not(mask1)
 
            cv2.imwrite("mask2/mask"+str(k)+".jpg",mask2)
            
            res1 = cv2.bitwise_and(img,img,mask=mask2)
            cv2.imwrite("res/res"+str(k)+".jpg",res1)
            
            res2 = cv2.bitwise_and(background, background, mask = mask1)
 
 
            
            final_output = cv2.addWeighted(res1,1,res2,1,0)
            
			rotated = ndimage.rotate(img, -90)
			cv2.imwrite("rotated1.jpg",rotated)
			
			cv2.imwrite("magic/magic"+str(k)+".jpg",rotated)
            cv2.imshow("magic",rotated)
			
            cv2.waitKey(1)
            
            k=k+1
            
            
            
            
            
            
            

def main():
    #recordFrames()
    redColorDetection()

if __name__=="__main__":
    main()