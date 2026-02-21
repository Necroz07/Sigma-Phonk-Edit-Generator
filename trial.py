import cv2
import math
import mediapipe as medpi

from mediapipe.tasks.python import vision
from mediapipe.tasks.python import BaseOptions

def distance(a, b):
    return math.hypot(a.x - b.x, a.y - b.y)

def smilescore(lms):
    left_corner = 61
    right_corner = 291
    upperlip = 13
    forehead = 10
    chin = 152

    avgcornery = (lms[left_corner].y + lms[right_corner].y) / 2

    lift = lms[upperlip].y - avgcornery   # bigger when corners rise

    face_height = abs(lms[chin].y - lms[forehead].y)

    normalizedlift = lift/face_height

    return normalizedlift

    #return avgcornery

baseopt = BaseOptions(model_asset_path="face_landmarker.task")
options = vision.FaceLandmarkerOptions(base_options=baseopt, num_faces=1)
detect = vision.FaceLandmarker.create_from_options(options)

cap = cv2.VideoCapture(3)
if not cap.isOpened():
    raise RuntimeError("can't open yo cam bro")

THRESH = -0.0  # start here. you will tune this.

smoothed = None
alpha = 0.2

while True:
    ok, frame = cap.read()
    if not ok:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_img = medpi.Image(image_format=medpi.ImageFormat.SRGB, data=rgb)
    result = detect.detect(mp_img)

    if not result.face_landmarks:
        cv2.putText(frame, "NO FACE", (99, 150), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 3)
        cv2.imshow("Webcam", frame)
        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            break
        continue

    lms = result.face_landmarks[0]
    score = smilescore(lms)

    smoothed = score if smoothed is None else (1 - alpha) * smoothed + alpha * score

    if smoothed > THRESH:
        text = f"SMILE DETECTED  {smoothed:.2f}"
    else:
        text = f"NO SMILE  {smoothed:.2f}"

    cv2.putText(frame, text, (60, 150), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 3)

    cv2.imshow("Webcam", frame)
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()