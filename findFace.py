import cv2
# 获取训练好的人脸的参数数据，这里直接从GitHub上使用默认值
face_cascade = cv2.CascadeClassifier(r"C:\Program Files\Python37\Lib\site-packages\cv2\data\haarcascade_eye.xml")
test = face_cascade.load(r"C:\Program Files\Python37\Lib\site-packages\cv2\data\haarcascade_eye.xml")

def findFace(frame):
    frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(frame_gray,1.3,5)
    print ("发现{0}个人脸!".format(len(faces)));
    hasFace = (len(faces) != 0);
    if hasFace:
        for(x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+w),(0,255,0),2)
    return frame, hasFace;
