import cv2
import numpy as np
# foto2 = cv2.imread("./goruntu/kanal.png")#klasörden görüntü okuma
# cv2.imshow("Kırmızı",foto2)
foto = cv2.imread("goruntu.jpg")
cv2.imshow("el",foto)
B = foto[:,:,0]
G = foto[:,:,1]
R = foto[:,:,2] #
# cv2.imshow("el1",B)
# # cv2.imshow("el2",G)
cv2.imshow("el3",R)
cv2.waitKey()
print(foto.shape)  # yükseklik, genişlik ve kanal sayısı
print(R.shape)
y = 4#sutun no
x=3 #satır no
kanal = 0
yogunluk_b= foto[y, x, kanal]
print("yoğunluk:",yogunluk_b)
yogunluk_r = R[y,x]
print("yoğunluk_gray:",yogunluk_r)
print("merhaba")
maksimum_yogunluk =np.max(B)
minimum_yogunluk =np.min(B)
print("Maksimum yoğunluk: ",maksimum_yogunluk)
print("Minimum yoğunluk: ",minimum_yogunluk)
print(foto[y,x])#tam koordinatın R G B değerleri döner