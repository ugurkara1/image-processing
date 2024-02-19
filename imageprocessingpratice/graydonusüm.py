import cv2
import numpy as np
# foto2 = cv2.imread("./goruntu/kanal.png")#klasörden görüntü okuma
# cv2.imshow("Kırmızı",foto2)
foto=cv2.imread("goruntu.jpg") #görüntü okuma
cv2.imshow("resim",foto)
#cv2.waitkey()
B=foto[:,:,0]
G=foto[:,:,1]
R=foto[:,:,2]
cv2.imshow("Mavi",B)
cv2.imshow("Yesil",G)
cv2.imshow("Kirmizi",R)
# # cv2.imshow("el1",B)
# cv2.imshow("el2",G)
#cv2.imshow("el3",R)
foto_gri=cv2.imshow("goruntu.jpg",0)
cv2.imshow("goruntu_gri",foto_gri)
# cv2.waitKey()
from  matplotlib import pyplot as plt
import matplotlib.image as mpimg
imgray=0.2989*R+0.5870*G+0.1140*R
cv2.imshow("gri_gösterim",imgray)
cv2.waitKey()
plt.imshow(imgray,cmap="gray")
plt.show()
cv2.waitKey()
print(foto.shape)  # yükseklik, genişlik ve kanal sayısı
print(R.shape)
x=4  #sütun no
y = 3 #satır no
kanal = 0
yogunluk_b= foto[y, x, kanal]
print("yoğunluk:",yogunluk_b)