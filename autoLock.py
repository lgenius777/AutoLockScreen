import findFace as finder;
import lockScreen as locker;
import cv2;
import collections


sampling_interval_ms =100;
cycle_ms = 10*1000;
sampling_site = int(cycle_ms/sampling_interval_ms);
recorder = collections.deque((1,),maxlen=sampling_site);

cap = cv2.VideoCapture(0)
index = 0;
lock_status = False;

while cap.isOpened():
    ret,frame = cap.read();
    frame_new, hasFace = finder.findFace(frame);
    c = cv2.waitKey(sampling_interval_ms);
    if hasFace == False : recorder.append(1);
    else : recorder.append(0);
    if lock_status == False :
        if recorder.count(1) > (sampling_site*0.8) :
            locker.lockScreen();
            lock_status = True;
        # cv2.imshow('Face Detector', frame_new);       
    else :
        if recorder.count(1) < (sampling_site*0.8) :
            lock_status = False;

cap.release()