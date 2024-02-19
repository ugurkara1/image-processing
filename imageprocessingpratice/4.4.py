import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread("hand.jpg",0)
# img = cv2.medianBlur(img,5)
ret,th1=cv2.threshold(img,80,255,cv2.THRESH_BINARY)
th2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
th3=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
#giriş görüntüsü, max değer, adaptif metot, eşikleme tipi,blok boyutu
titles = ['Original Image', 'Global Thresholding (v = 90)', 'Adaptif ortalama esikleme', 'Adaptif Gaussian esikleme']
images = [img, th1, th2, th3]
for i in range(4):
    plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()