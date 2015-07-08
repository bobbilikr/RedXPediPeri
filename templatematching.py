
import numpy as np
import cv2
 
image = cv2.imread('afs.jpg')
imageColor = cv2.imread('afs.jpg')
template = cv2.imread('as.jpg')
 
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
h,w = template.shape
 
result = cv2.matchTemplate(image,template, cv2.TM_CCOEFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
 
cv2.rectangle(imageColor,top_left, bottom_right,(0,0,255),6)
 
cv2.imshow("Result", imageColor)
cv2.waitKey(0)
