import cv2

import numpy as np


def click(event,x,y,flags,param):
        if event == cv2.EVENT_LBUTTONUP:
            cv2.circle(ima,(x,y),3,(255,0,0),-1)
            
            list1.append((x,y))
            if len(list1) >= 2:
                cv2.line(ima,list1[-2],list1[-1],(255,0,0),5)
            cv2.imshow("frame",ima)
        
        if event == cv2.EVENT_RBUTTONUP:
            b = ima[y,x , 0]
            g = ima[y,x , 1]
            r = ima[y,x , 2]
            
            ima1 = np.zeros((512,512,3),np.uint8)
            ima1[:] = [b,g,r]
            cv2.imshow("charan",ima1)
            
# ima = cv2.imread("C:\\Users\\USER\\Pictures\\png_test_punda.png") 
     
ima = np.zeros((1000,1000,3),np.uint8)
cv2.imshow("frame",ima)
list1 = []
cv2.setMouseCallback("frame",click)
cv2.waitKey(0)
cv2.destroyAllWindows()
