import cv2

# image read flags 0 for grey scale ,1 colored image ,-1 loads image including its alpha channel
img = cv2.imread('2e32b4c96a8d8f10.jpg',0)

# prints matrix
print(img)

# show image for mili-second
cv2.imshow('My Dog Image Frame',img)

# delay image show by 5 seconds but if 0 secs will close when user press cancel window button
# cv2.waitKey(5000)
# cv2.waitKey(0)


# close window if user press certain key
k = cv2.waitKey(0)
# k is the escape key
if k == 27:
    cv2.destroyAllWindows()

# if s key is pressed image is saved
elif k == ord('s'):
    cv2.imwrite('mydog.png', img)



# destroys all windows
# cv2.destroyAllWindows()



# write file to certail location,,(new image file extension , image you want to save)
# cv2.imwrite('mydog.png',img)