import cv2
import numpy as np

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

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #gray = np.float32(gray)

    lower_blue = np.array([90,100,100])
    upper_blue = np.array([110,225,225])

    lower_green = np.array([60,100,100])
    upper_green = np.array([80,255,255])

    lower_yellow = np.array([30, 50, 50])
    upper_yellow = np.array([50, 255, 255])

    lower_white = np.array([0, 0, 150])
    upper_white = np.array([255, 50, 255])

    lower_red = np.array([245, 20, 100])
    upper_red = np.array([10, 255, 255])

    # Threshold the HSV image to get onlycolors
    mask0 = cv2.inRange(hsv, lower_blue, upper_blue)
    mask1 = cv2.inRange(hsv, lower_green, upper_green)
    mask2 = cv2.inRange(hsv, lower_yellow, upper_yellow)
    mask3 = None
    mask4 = cv2.inRange(hsv, lower_red, upper_red)
    mask5 = None

    fmask = mask0
    fmask = cv2.add(fmask, mask1)
    fmask = cv2.add(fmask, mask2)
    #fmask = cv2.add(fmask, mask3)
    fmask = cv2.add(fmask, mask4)
    #fmask = cv2.add(fmask, mask5)
    #mask = cv2.threshold(gray, 50, 200, 0)[1]
    #res = frame


    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= fmask)

    #mask = cv2.bilateralFilter(mask, 5, 10, 10)
    contours, hierarchy = cv2.findContours(fmask, 1, 2)
    squareLoc = [0,0,0,0,0,0,0,0,0]
    try:
        cnt = contours[0]
        contourcount = 0
        for cnt in contours:
            #cv2.drawContours(res, cnt, -1, (255, 255, 255), 2)
            x,y,w,h = cv2.boundingRect(cnt)
            ratio = np.float32(np.float32(w)/np.float32(h))
            if (0.8 < ratio < 1.25) and (h > 15) and (w > 15):
                cv2.rectangle(res,(x,y),(x+w,y+h),outline[contourcount],2)
                cv2.putText(res,str(-contourcount +9), (x + (w/2), y + (h/2)), cv2.FONT_HERSHEY_PLAIN, 2, 255)
                M = cv2.moments(cnt)
                squareLoc[contourcount] = [int(M['m10']/M['m00']), int(M['m01']/M['m00'])]
                contourcount += 1

    except Exception as e:
        pass

    squareLoc = sorted(squareLoc)
    '''try:
        center = ((squareLoc[3][0] + squareLoc[5][0]) / 2), ((squareLoc[3][1] + squareLoc[5][1]) / 2)
        print center
        print hsv[center]
    except Exception as e:
        pass'''
    #print (squareLoc[3][0] + squareLoc[4][0])/2
    #print contourcount
    contourcount = 0
    #cv2.drawContours(res, [box], 0, (0, 0, 255), 2)

    cv2.imshow('frame',frame)
    #cv2.imshow('mask',fmask)
    #cv2.imshow("uh", dst)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
