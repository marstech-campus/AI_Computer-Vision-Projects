import cv2 #import openv library
import imutils #import imutils library

lion= cv2.imread("image1.png") # read image

sizelion=imutils.resize(lion,width=500,height=700) # resize image

cv2.imwrite("500px.png", sizelion) # Write Image


cv2.destroyAllWindows()
