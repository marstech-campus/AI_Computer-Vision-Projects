import cv2 

img = cv2.imread("image1.png")

GBimg = cv2.GaussianBlur (img, (35,35),15)

cv2.imwrite("BluredImage2.jpg", GBimg)

cv2.destroyAllWindows()
