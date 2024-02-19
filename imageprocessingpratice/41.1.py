#görüntü inverting,positive/negative transforms
import cv2
import numpy as np
from matplotlib import pyplot as plt
image=cv2.imread("hand.jpg",0)#griye çevirme
#max=np.max(image)-image #görüntüdeki en büyük piksel parlaklığını verir
inverted=np.invert(image)#tersini aldırma
cv2.imshow("original",image)
cv2.imshow("inverted",inverted)
#cv2.waitkey()
negimage=255-image#görüntünün negatifini verir

cv2.imshow("negimage",negimage)
cv2.waitKey()