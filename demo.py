import findFace as finder;
import lockScreen as locker;
import cv2;
cap = cv2.VideoCapture(0)
index = 0;

while cap.isOpened():
    ret,frame = cap.read()
    frame_new, hasFace = finder.findFace(frame);
    cv2.imshow('Face Detector', frame_new)
    c = cv2.waitKey(100)
    if c == 27:
        break;

cap.release()