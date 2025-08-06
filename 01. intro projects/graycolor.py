import cv2

lion= cv2.imread("image1.png")

graylion=cv2.cvtColor(lion, cv2.COLOR_BGR2GRAY)

cv2.imwrite("Gray.png", graylion)

cv2.destroyAllWindows()
