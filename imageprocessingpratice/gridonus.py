import cv2
foto = cv2.imread("goruntu.jpg")
cv2.imshow("el",foto)
B = foto[:,:,0]
G = foto[:,:,1]
R = foto[:,:,2]
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
imGray=0.2989*R+0.5870*G+0.1140*B
plt.imshow(imGray,cmap="gray")
plt.show()