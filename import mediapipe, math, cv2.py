from mediapipe.tasks.python import BaseOptions
from mediapipe.tasks.python import vision
import time, cv2, mediapipe as medpi

def smilescore(lms):

    left_corner=61
    right_corner=291
    chin=152
    forehead=10
    upper_lip=13

    avgycorner = (lms[left_corner].y + lms[right_corner].y)/2
    faceheight = abs(lms[chin].y - lms[forehead].y)

    lift = lms[upper_lip].y - avgycorner

    normalizedlift = lift/faceheight

    return normalizedlift

baseopt = BaseOptions(model_asset_path='face_landmarker.task')
options = vision.FaceLandmarkerOptions(base_options=baseopt, num_faces=1)
detect = vision.FaceLandmarker.create_from_options(options)

cap = cv2.VideoCapture(3)

currenttime = None
waittime = 3

thresh= -0.0001

if not cap.isOpened():
    raise RuntimeError("can't open yo cam bro")

while True: 
    ok, frame = cap.read()
    
    if not ok:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_img = medpi.Image(image_format=medpi.ImageFormat.SRGB, data=rgb)
    result = detect.detect(mp_img)

    if not result.face_landmarks:
        cv2.putText(frame, "No Face", (99, 150), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 3)
        cv2.imshow("CAM", frame)

        if cv2.waitKey(1) == ord('q'):
            break
        continue

    lms = result.face_landmarks[0]

    score = smilescore(lms)

    if score > thresh:
        if currenttime is None:
            currenttime = time.time()

        if (time.time() - currenttime) > waittime:

            cv2.putText(frame, f"SMILE DETECTED {score}", (99, 150), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 3)
            cv2.imshow("CAM", frame)
        
            if cv2.waitKey(500) == ord('q'):
                break

    else:
        cv2.imshow("CAM", frame)
        if cv2.waitKey(1) == ord('q'):
            break
        currenttime= None


    if cv2.waitKey(1) == ord('q'):
            break
    
cap.release()
cv2.destroyAllWindows()
