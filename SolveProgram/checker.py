import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    frame = cv2.GaussianBlur(frame, (25, 25), 0)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #ret, corners = cv2.findChessboardCorners(gray, (3, 3), None)

    cv2.imshow("img", frame)
    cv2.imshow("okay", gray)


    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
