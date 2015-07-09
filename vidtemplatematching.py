import numpy as np
import cv2
import time
 
cap = cv2.VideoCapture(0)#'output.avi')

#image = cv2.imread('afs.jpg')
#imageColor = cv2.imread('afs.jpg')
#template = cv2.imread('as.jpg')
 
ret, old_frame = cap.read()
template = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)

rows = len(template)
cols = len(template[0])
#print rows
#print cols
template = template[230:250, 310:330];

center = (240, 320)
#print center

while(1):
	ret,frame = cap.read()
	image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)	

	h,w = template.shape
	
	result = cv2.matchTemplate(image,template, cv2.TM_CCOEFF_NORMED)
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
	top_left = max_loc
	#print top_left
	bottom_right = (top_left[0] + w, top_left[1] + h)
	#bottom_right tells cols first & then rows, cols from left to right and rows from top to bottom

	center_pixel = (top_left[0] + w/2, top_left[1] + h/2)

	deviation_in_pixels = (center_pixel[0] - center[0], center_pixel[1] - center[1])

	#print deviation_in_pixels

	#print bottom_right
	cv2.rectangle(frame,top_left, bottom_right,(0,0,255),6)
	cv2.imshow("Result", frame)

	cv2.waitKey(20)
