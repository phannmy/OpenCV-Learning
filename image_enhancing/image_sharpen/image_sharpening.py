import cv2
import numpy as np

#this kernel may be edge detection kernel
kernel = np.array([[-1,-1,-1],
                 [-1,9,-1], 
                 [-1,-1,-1]])
kernel2 = np.array([[0,-1,0],
                    [-1,5,-1],
                    [0,-1,0]])
picture = cv2.imread("picture.jpg")
cv2.imshow("picture", picture)
cv2.waitKey()

#not sure if this is edge detection
basic_Sharpening = cv2.filter2D(picture, -1, kernel)
cv2.imshow("basic sharpening", basic_Sharpening)
cv2.waitKey()

sharpening = cv2.filter2D(picture,-1,kernel2)
cv2.imshow("sharpening?", sharpening)
cv2.waitKey()