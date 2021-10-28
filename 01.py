import cv2
import numpy as np

red = (0,0,255)
img = cv2.imread(r"C:\Users\Shreyas Desai\Desktop\stool.png", 1)
img = cv2.resize(img,(400,400))
img = cv2.flip(img,-1)
canvas = np.zeros((300,300,3), dtype="uint8")*255
canvas = cv2.circle(canvas,(40,40),20,red,-1)
canvas = cv2.circle(canvas,(0,0),(200,200),red,2)
#canvas[:]=(0,0,255)
cv2.imshow(".",img)
cv2.waitKey(0)