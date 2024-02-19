import cv2
import matplotlib.pyplot as plt
import numpy as np
def log_donusum(r,c):
    r=r.astype(float)
    s=c * np.log(1 + r)
    return s.astype(np.uint8)
foto=cv2.imread("monografi.jpg",0)
logaritma=log_donusum(foto,c=1)
plt.imshow(logaritma,cmap="gray")
plt.show()