import cv2
import time


def runcam():
    capture = cv2.VideoCapture(0)

    if not capture.isOpened():
        raise RuntimeError("cant open yo cam bro")

    while True:
        ok, frame = capture.read()

        if not ok:
            break

        cv2.imshow("4k hd footage", frame)
        key = cv2.waitKey(1)

        if key == ord('q') or key == ord('Q'):
            break
    
    capture.release()
    cv2.destroyAllWindows()

runcam()