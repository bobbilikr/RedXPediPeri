import numpy as np
import cv2

cap = cv2.VideoCapture(0)   #use 0 / 1 for webcam or others

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')

#Parameters(filename, fourcc{codecs}, fps, frame_size, is_color=1 {default color})
out = cv2.VideoWriter('output.avi',fourcc, 30.0, (640,480))

#while capturing video, if want to off use Ctrl+C
while(cap.isOpened()):
    ret, frame = cap.read() #ret is true implies capturing works
    if ret==True:

        # write the frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
