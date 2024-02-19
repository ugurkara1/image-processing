import cv2
import matplotlib.pyplot as plt
import numpy as np
def fotonegative(foto):
    L=np.max(foto)
    negatif_foto=L-foto
    return negatif_foto
foto=cv2.imread("monografi.jpg",0)
cv2.imshow("foto1",foto)
negatif_foto=fotonegative(foto)
plt.imshow(negatif_foto,cmap="gray")
plt.show()