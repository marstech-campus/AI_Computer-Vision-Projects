import cv2

lion= cv2.imread("image1.png")

cv2.imwrite("sampleimage.jpg", lion)


cv2.destroyAllWindows()
