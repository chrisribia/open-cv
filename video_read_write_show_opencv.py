import cv2

# capture image from camera ,,you can privide your camera index eg 0 for camera or provide video file path
cap = cv2.VideoCapture(0)

# video writer

# specifie video codeac
fourcc = cv2.VideoWriter_fourcc('X','V','1','D')
# 20.0 number of frames per sec
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

# capture video frame continiously

# While(cap.isOpened())... checks if file path is valid to return true or false
while(True):



    # ret save true or flalse
    # frame return frame from cap.read()
    ret,frame = cap.read()

    if ret == True:

        # get height of the frame.
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        # get width of the frame.
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        print(height, width)
        out.write(frame)
        # change image form coloured to grey scale
        grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        cv2.imshow('Image Frame',grey)

        # 0xFF  mask required for 64bit computer
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
# need to rease resources ..camera
cap.release()
out.release()
cv2.destroyAllWindows()

