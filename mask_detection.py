from tensorflow.keras.applications.mobilenet_v3 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from imutils.video import VideoStream
import numpy as np
import time,imutils
import cv2
import os
from tensorflow.python.keras.backend import clear_session, prod, shape
def detect_and_predict_mask(frame,faceNet,maskNet):
    (h,w)=frame.shape[:2]
    blob=cv2.dnn.blobFromImage(frame,1.0,(224,224),(104.0,177.0,123.0))
    faceNet.setInput(blob)
    detections=faceNet.forward()
    print(detections,shape)
    faces=[]
    locs=[]
    preds=[]
    for i in range(0,detections.shape[2]):
        confidence=detections[0,0,i,2]
        if confidence >0.5:
            box=detections[0,0,i,3:7]*np.array([w, h, w, h])
            (startX,startY,endX,endY)=box.astype("int")
            (startX,startY)=(max(0,startX),max(0,startY))
            (endX,endY)=(min(w-1,endX),min(h-1,endY))
            face=frame[startY:endY,startX:endX]
            face=cv2.cvtColor(face,cv2.COLOR_BGR2RGB)
            face=cv2.resize(face,(224,224))
            face=img_to_array(face)
            face=preprocess_input(face)
            faces.append(face)
            locs.append(startX,startY,endX,endY)

    if len(faces) >0:
        faces=np.array(faces,dtype="float32")
        preds=maskNet.predict(faces,batch_size=32)
    return (locs,preds)
protoxpath=r"face_detector/deploy.prototxt"
weightspath=r"face_detector/res10_300x300_ssd_iter_140000.caffemodel"
faceNet=cv2.dnn.readNet(protoxpath,weightspath)
maskNet=load_model("mask_detector.model")
print("[INFO] starting video stream")
vs=VideoStream(src=0).start()
while True:
    frame=vs.read()
    frame=imutils.resize(frame,width=400)
    (locs,preds)=detect_and_predict_mask(frame,faceNet,maskNet)
    for (box,prod) in zip(locs,preds):
        (startX,startY,endX,endY)=box
        (mask,withoutMask)=preds
        label= "Mask" if mask>withoutMask else "No Mask"
        color=(0,225,0) if label == "Mask" else (0,0,225)

        label="{}: {:.2f}%".format(label,max(mask,withoutMask)*100)

        cv2.putText(frame,label,(startX,startY-10),cv2.FONT_HERSHEY_SIMPLEX,0.45,color,2)
        cv2.rectangle(frame,(startX,startY),(endX,endY),color,2)
    cv2.imshow("Frame",frame)
    key=cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

cv2.destroyAllWindows()
vs.stop()