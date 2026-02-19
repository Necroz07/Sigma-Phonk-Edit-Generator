import cv2
import math

import mediapipe as medpi

from mediapipe.tasks.python import vision
from mediapipe.tasks.python import BaseOptions



def distance(a, b):
    distx = a.x - b.x
    disty = a.y - b.y

    return math.hypot(distx, disty)


def smilescore(lms):

    left_corner = 61
    right_corner = 291
    upperlip = 13
    lowerlip = 14
    
    w = distance(lms[left_corner], lms[right_corner])
    h = distance(lms[upperlip], lms[lowerlip])

    mar = w/(h + 1e-6)
    return mar

baseopt = BaseOptions(model_asset_path="face_landmarker.task")
options = vision.FaceLandmarkerOptions(base_options = baseopt, num_faces = 1)
detect = vision.FaceLandmarker.create_from_options(options)

capt= cv2.VideoCapture(3)

if not capt.isOpened():
    raise RuntimeError("can't open yo cam bro")

while True:
    ok, frame = capt.read()
    if not ok:
        break

    mp_img= medpi.Image(image_format=medpi.ImageFormat.SRGB, data=frame)

    result = detect.detect(mp_img)

    '''
    if result.face_landmarks:
        cv2.putText(frame, "FACE DETECTED", (99, 150), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 3)

        print(f"Landmarks= {len(result.face_landmarks[0])}") '''

    lms = result.face_landmarks[0]
    score = smilescore(lms)

    if score > 18.0:
        cv2.putText(frame, "SMILE DETECTED", (99, 150), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 3)

    else:
        cv2.putText(frame, "NO SMILE DETECTED", (99, 150), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 3)




    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1)==ord('q'):
        break

capt.release()
cv2.destroyAllWindows()