import cv2
import datetime

# capture video from device camera
cap = cv2.VideoCapture(0)

# print video width and height
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

# set frame
# cap.set(3,3000)
# cap.set(4,3000)
#
# print(cap.get(3))
# print(cap.get(4))
while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:

        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width: '+str(cap.get(3))+' Height: '+str(cap.get(4))
        datet = str(datetime.datetime.now())
        frame = cv2.putText(frame,datet,(10,50),font,1,(0,255,255))
        # 1 is for font scale

        cv2.imshow("frame", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            # close frame iff user press q ...
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()

