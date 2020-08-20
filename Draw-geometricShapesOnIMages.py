import numpy as np
import cv2
# img = cv2.imread('31062468.jpg',1)

# create numpy image
img = np.zeros([512,512,3],np.uint8)

# Draw straight line
img = cv2.line(img, (0,0),(255,255), (147,96,44), 10)

#Draw arrowed line
img = cv2.arrowedLine(img, (0,255),(255,255), (147,96,44), 10)


# Draw rectangle
img = cv2.rectangle(img, (355,255), (255,128), (0,0,255),10)


# Draw circle
img = cv2.circle(img, (355,255), 36, (0, 255, 0), -1)


# Text in an Image
font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img,"Chrisribia Open Cv",(0,255),font, 4,(255,0,0), 1,cv2.LINE_AA)
cv2.imshow("image liv\ne",img)
cv2.waitKey(0)
cv2.destroyAllWindows()