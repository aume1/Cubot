import cv2
import numpy as np
import math

cap = cv2.VideoCapture(0)

outline = [
    (0, 25, 225),
    (0, 50, 200),
    (0, 75, 175),
    (0, 100, 150),
    (0, 125, 125),
    (0, 150, 100),
    (0, 175, 75),
    (0, 200, 50),
    (0, 225, 25)
]

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsvOrig = hsv

    # HSV Green
    lower_green = np.array([60, 50, 50])
    upper_green = np.array([90, 200, 225])

    # HSV Red
    lower_red = np.array([0, 50, 50])
    upper_red = np.array([255, 255, 255])

    # Old green
    #lower_green = np.array([40,100,50])
    #upper_green = np.array([120,255,150])

    # Color number stuff
    # lower_blue = np.array([90,100,100])
    # upper_blue = np.array([110,225,225])
    #
    # lower_yellow = np.array([30, 50, 50])
    # upper_yellow = np.array([50, 255, 255])
    #
    # lower_white = np.array([0, 0, 150])
    # upper_white = np.array([255, 50, 255])
    #
    # lower_red = np.array([245, 20, 100])
    # upper_red = np.array([10, 255, 255])

    # Blur and smooth image
    hsv = cv2.bilateralFilter(hsv, 5, 10, 10)
    hsv = cv2.medianBlur(hsv, 5)

    # Threshold the HSV image to get onlycolors
    fmask = cv2.inRange(hsv, lower_green, upper_green)
    fmask = cv2.add(fmask, cv2.inRange(hsv, lower_red, upper_red))

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= fmask)

    # Erode res
    kernel = np.ones((7, 7), np.uint8)
    res = cv2.erode(res, kernel, iterations = 1)
    res = cv2.dilate(res, kernel, iterations = 1)

    contours, hierarchy = cv2.findContours(fmask, 1, 2)

    squareLoc = [0,0,0,0,0,0,0,0,0]


    try:
        cnt = contours[0]
        contourcount = 0
        for cnt in contours:
            x,y,w,h = cv2.boundingRect(cnt)
            ratio = np.float32(np.float32(w)/np.float32(h))
            if (0.8 < ratio < 1.25) and (h > 15) and (w > 15):
                cv2.putText(res,str(-contourcount +9), (x + (w/2), y + (h/2)), cv2.FONT_HERSHEY_PLAIN, 2, 255)
                M = cv2.moments(cnt)
                squareLoc[contourcount] = [int(M['m10']/M['m00']), int(M['m01']/M['m00'])]
                center = (squareLoc[contourcount][0], squareLoc[contourcount][1])

                rect = cv2.minAreaRect(cnt)
                box = cv2.cv.BoxPoints(rect)
                box = np.int0(box)
                cv2.drawContours(res,[box],0,outline[contourcount],2)
                print str(hsvOrig[center[0], center[1]]) + " " + str(contourcount)
                contourcount += 1

    except Exception as e:
        pass

    squareLoc = sorted(squareLoc)
    contourcount = 0

    cv2.imshow('frame',frame)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
