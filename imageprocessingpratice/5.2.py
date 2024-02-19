import cv2
import numpy as np
image=cv2.imread("einstein.jpg")
blur_filter1=np.ones((3,3))/(9.0)
image_blur1=cv2.filter2D(image,-1,blur_filter1)
gaussian_blur=cv2.GaussianBlur(image,(3,3),0)
median_filtre=cv2.medianBlur(image,3)
cv2.imshow("original",image)
cv2.imshow("gaussian filtre soncu",gaussian_blur)
cv2.imshow("medyan filtre sonucu blurred",median_filtre)
cv2.waitKey()