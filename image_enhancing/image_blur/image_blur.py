import cv2

a = cv2.imread('./img/RawData.jpg')
cv2.imshow('img', a)
cv2.waitKey(0)

filter2d = cv2.filter2D(a, -1, (5,5))
cv2.imshow("filter 2d", filter2d)
cv2.waitKey(0)

Gaussian = cv2.GaussianBlur(a, (7,7), 0)
cv2.imshow("Gaussian Blur", Gaussian)
cv2.waitKey(0)

median = cv2.medianBlur(a, 5)
cv2.imshow("Median Blur", median)   
cv2.waitKey(0)

bilateral = cv2.bilateralFilter(a, 9, 75, 75)
cv2.imshow("Bilateral Blur", bilateral)
cv2.waitKey(0)