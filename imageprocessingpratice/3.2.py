import cv2
import numpy as np
from matplotlib import pyplot as plt
foto1=cv2.imread("hand.jpg",0)
import matplotlib.image as mpimg
#michalsonın denklemi ile contrast iyileştirme
CM=(np.max(foto1)-np.min(foto1)/np.max(foto1)+np.min(foto1))
yeni= CM*foto1
plt.imshow(yeni,cmap="gray")
plt.show()
cv2.imshow("hand.original",foto1)
cv2.waitKey()
#iyileştirilen görüntü ile orjinalin histogram karşılastırması
hist_gray=cv2.calcHist([foto1],[0],None,[256],[0,256])#gri görüntü hesaplama
hist_gray_yeni=cv2.calcHist([yeni],[0],None,[256],[0,256])
plt.figure(1)
plt.plot(hist_gray)

plt.figure(2)
plt.plot(hist_gray_yeni)
plt.show()