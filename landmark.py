import cv2
import dlib
import numpy as np

PREDICTOR_PATH = "/home/xavier/dlib-18.18/shape_predictor_68_face_landmarks.dat"
predictor = dlib.shape_predictor(PREDICTOR_PATH)
cascade_path='/home/xavier/opencv/opencv-2.4.10/data/haarcascades/haarcascade_frontalface_default.xml'
cascade = cv2.CascadeClassifier(cascade_path)

def get_landmarks(im):
    rects = cascade.detectMultiScale(im, 1.3,5)
    x,y,w,h =rects[0].astype(long)
    rect=dlib.rectangle(x,y,x+w,y+h)
    return np.matrix([[p.x, p.y] for p in predictor(im, rect).parts()])

def annotate_landmarks(im, landmarks):
    im = im.copy()
    for idx, point in enumerate(landmarks):
        print idx, point
        pos = (point[0, 0], point[0, 1])
        cv2.putText(im, str(idx), pos,
                    fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
                    fontScale=0.4,
                    color=(0, 0, 255))
        cv2.circle(im, pos, 3, color=(0, 255, 255))
    return im

def test(im):
    x,y=im.shape[:2]
    rect=dlib.rectangle(0,0,x,y)
    lm=[]
    for p in predictor(im,rect).parts():
        print p.x,p.y
        #lm.append(im[p.x,p.y])
    print lm
    return np.matrix([[p.x,p.y] for p in predictor(im,rect).parts()])


#im=cv2.imread('../LFW_big_train_resized/Abdullah_Gul/1Abdullah_Gul_0001.jpg')
#im=cv2.imread('../AR_matlab/M-001-01.bmp')
im=cv2.imread('../photomoi.jpg')
#cv2.imshow('img',im)
cv2.imshow('Result',annotate_landmarks(im,get_landmarks(im)))
#cv2.imshow('Result',annotate_landmarks(im,test(im)))
cv2.waitKey(0)
cv2.destroyAllWindows()
