import numpy as np
import cv2

tol = 100

#blue = [120, 90, 30]
#green = [100, 200, 50]
#white = [200, 200, 200]
#yellow = [50, 200, 200]
#red = [0, 0, 150]
#orange = [30, 100, 255]

blue = [255, 0, 0]
green = [0, 255, 0]
white = [255, 255, 255]
yellow = [0, 255, 255]
red = [0, 0, 255]
orange = [0, 255, 255]

'''bluetol = ([blue[0] - tol, blue[1] - tol, blue[2] - tol], [blue[0] + tol, blue[1] + tol, blue[2] + tol])
greentol = ([green[0] - tol, green[1] - tol, green[2] - tol], [green[0] + tol, green[1] + tol, green[2] + tol])
whitetol = ([white[0] - tol, white[1] - tol, white[2] - tol], [white[0] + tol, white[1] + tol, white[2] + tol])
yellowtol = ([yellow[0] - tol, yellow[1] - tol, yellow[2] - tol], [yellow[0] + tol, yellow[1] + tol, yellow[2] + tol])
redtol = ([red[0] - tol, red[1] - tol, red[2] - tol], [red[0] + tol, red[1] + tol, red[2] + tol])
orangetol = ([orange[0] - tol, orange[1] - tol, orange[2] - tol], [orange[0] + tol, orange[1] + tol, orange[2] + tol])'''



boundaries = [
    blue,
    green,
    white,
    yellow,
    red,
    orange
]

width = 200
height = 200

cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2)

    i = 0
    p = 0
    imageLayer = [0,0,0,0,0,0]

    for color in boundaries:

        lower = [color[0] - tol, color[1] - tol, color[2] - tol]
        upper = [color[0] + tol, color[1] + tol, color[2] + tol]

        p = 0

        for num in lower:
            if num < 0:
                lower[p] = 0
            p += 1

        p = 0

        for num in upper:
            if num > 255:
                upper[p] = 255
            p += 1


        lower = np.array(lower, dtype = "uint8")
        upper = np.array(upper, dtype = "uint8")

        crop = frame#[10:110, 10:110]

        crop = cv2.bilateralFilter(crop, 5, 15, 15)
        #crop = cv2.medianBlur(crop, 5)



        mask = cv2.inRange(crop, lower, upper)

        output = frame

        output = cv2.bitwise_and(crop, crop, mask = mask)
        #output = cv2.add(output, cropoutput)

        #output[np.where((output != [0,0,0]).all(axis = 2))] = color

        imageLayer[i] = output



        k = imageLayer[i]
        k = cv2.add(imageLayer[0],k)
        k = cv2.add(imageLayer[1],k)
        k = cv2.add(imageLayer[2],k)
        k = cv2.add(imageLayer[3],k)
        k = cv2.add(imageLayer[4],k)
        k = cv2.add(imageLayer[5],k)

        #im2, contours, hierarchy = cv2.findContours(k,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        #cv2.drawContours(k, contours, 3, (255, 255, 255), 3)


        i += 1

        #cv2.rectangle(frame, (10, 10), (110, 110), (255, 255, 255), 2)

        grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(grayframe, 5, 255, 0)
        uh = thresh
        contours, hierarcy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        if (len(contours) > 0):
            cv2.drawContours(frame, contours, -1, (255,255,255), 1)

        cv2.imshow("uh", np.hstack([frame, crop, k]))
        cv2.imshow("k", uh)
        #cv2.imshow("image", np.hstack([frame]))

    print frame[0, 0]


    '''for x in range(width):
        for y in range(height):
            px = frame[x, y][0]
            if px in range(100, 150):
                frame[x, y] = [255, 255, 255]'''

    #for frame[][0] in range(frame, [100, 60, 10], [120, 80, 30], frame)


    # Display the resulting frame

    #print frame[0,0]
    #cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
