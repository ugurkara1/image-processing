import cv2
import numpy as np
image=cv2.imread("einstein.jpg",0)
blur_filter1=np.ones((3,3))/(9.0)
blur_filter2=np.ones((8,8))/(64.0)
blur_filter3=np.ones((10,10))/(100.0)
image_blur1=cv2.filter2D(image,-1,blur_filter1)
image_blur2=cv2.filter2D(image,-1,blur_filter2)
image_blur3=cv2.filter2D(image,-1,blur_filter3)
cv2.imshow("foto1",image)
cv2.imshow("foto2",image_blur1)
cv2.imshow("foto3",image_blur2)
cv2.imshow("foto4",image_blur3)
cv2.waitKey(0)