import numpy as   np
import cv2

# print all events packages
# event = [i for i in dir(cv2) if 'EVENT' in i]
# print(event)

# mouse call back
def click_env(event, x, y, flags,param):
    # event on mouse
    # x,y coordinate for the image
    # flags
    # param
    if event == cv2.EVENT_LBUTTONDOWN:
        # left click mouse
        print(x,', ',y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x)+', '+str(y)
        cv2.putText(img,strXY,(x,y), font, 0.5, (255,255,0),2)
        cv2.imshow('image', img)
    if event == cv2.EVENT_RBUTTONDOWN:
        # Right click mouse
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]

        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ', ' + str(green)+ ', ' + str(red)
        cv2.putText(img, strBGR, (x, y), font, 0.5, (255, 255, 0), 2)
        cv2.imshow('image', img)



# img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread('2e32b4c96a8d8f10.jpg')

cv2.imshow('image', img)

cv2.setMouseCallback('image', click_env)
cv2.waitKey(0)
cv2.destroyAllWindows()