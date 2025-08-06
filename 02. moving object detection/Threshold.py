import cv2

img = cv2.imread("image1.png")

grayimg =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

thimg = cv2.threshold(grayimg, 180 ,255,cv2.THRESH_BINARY)[0]

cv2.imwrite("Thresholdimage2.png", thimg)

cv2.destroyAllWindows()
