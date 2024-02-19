import cv2
import numpy as np
import math
from matplotlib import pyplot as plt
img=cv2.imread("lion.jpeg")
#görüntüyü gri seviyeye dönüştür
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#gamma değerini otomatik hesaplama=log(mid*255)/log(mean)
mid=0.5
mean=np.mean(gray)
gamma=math.log((mid*255)/math.log(mean))
#gamma düzeltmesi
img_gamma1=np.power(img,gamma).clip(0,255).astype(np.uint8)
cv2.imshow("orijinal",img)
cv2.imshow("sonuc",img_gamma1)
cv2.waitKey(0)
