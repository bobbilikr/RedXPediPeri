
import numpy as np
import cv2
import time
 
cap = cv2.VideoCapture(0)#'output.avi')


ret, old_frame = cap.read()
template = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)

rows = len(template)
cols = len(template[0])
#print rows
#print cols
template = template[230:250, 310:330];

while(1):
	ret,frame = cap.read()
	image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)	

	h,w = template.shape
	result = cv2.matchTemplate(image,template, cv2.TM_CCOEFF_NORMED)
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
	top_left = max_loc
	bottom_right = (top_left[0] + w, top_left[1] + h)
	cv2.rectangle(frame,top_left, bottom_right,(0,0,255),6)
	cv2.imshow("Result", frame)

	cv2.waitKey(20)
