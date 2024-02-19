import cv2
import matplotlib.pyplot as plt
import  numpy as np
img=cv2.imread("einstein.jpg",0)
equ=cv2.equalizeHist(img)
res=np.hstack((img,equ))
#histogramları kıyaslama
hist1=cv2.calcHist([img],[0],None,[256],[0,256])
hist2=cv2.calcHist([equ],[0],None,[256],[0,256])
plt.figure(1)
plt.plot(hist1)
plt.figure(2)
plt.plot(hist2)
cv2.imshow("image", res)
cv2.waitKey(0)
cv2.destroyAllWindows()