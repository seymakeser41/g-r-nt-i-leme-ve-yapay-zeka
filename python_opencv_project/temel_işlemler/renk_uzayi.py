import cv2
import numpy as np

img=cv2.imread("newresim.jpg")
img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)#Resmi 3 farklı renk uzayına dönüştürüp görüntüledik
img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("resim",img)
cv2.imshow("resim1",img_rgb)
cv2.imshow("resim2",img_hsv)
cv2.imshow("resim3",img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()