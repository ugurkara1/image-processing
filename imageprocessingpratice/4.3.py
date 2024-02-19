#log dönüşümü
import cv2
import numpy as np
from matplotlib import pyplot as plt
image1=cv2.imread("lion.jpeg")
cv2.imshow("original",image1)
# print(image1.dtype)
c=255/np.log(1+np.max(image1))
log_image=35*np.log(1+image1)
log_image=np.array(log_image,dtype=np.uint8))#imshow ile gösterebilmek için uint8 yapmalıyız
cv2.imshow("logaritmik dönüşümler",log_image)#değerler çok küçük, birşey görünmez. 255 e bölmek gerekiyor
cv2.waitKey()
# log_image = 255/(c*np.log(1+image1))
# log_image = np.array(log_image, dtype = np.uint8)#imshow ile gösterebilmek için uint8 yapmalıyız
# cv2.imshow("Logaritmik Dönüşüm_255", log_image)