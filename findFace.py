import os;
import cv2;
cv_lib_path = os.path.dirname(cv2.__file__);
haarcascade_path = os.path.join(cv_lib_path, "data", "haarcascade_eye.xml");
face_cascade = cv2.CascadeClassifier(haarcascade_path);
test = face_cascade.load(haarcascade_path);

def findFace(frame):
    frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(frame_gray,1.3,5)
    print ("Find {0} target!".format(len(faces)));
    hasFace = (len(faces) != 0);
    if hasFace:
        for(x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+w),(0,255,0),2)
    return frame, hasFace;
