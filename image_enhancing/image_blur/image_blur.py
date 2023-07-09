import cv2


a = cv2.imread('./img/RawData.jpg')
cv2.imshow('img', a)
cv2.waitKey()