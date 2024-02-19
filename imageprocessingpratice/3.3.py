import cv2
import matplotlib.pyplot as plt
#RGB bantlarının histogramlarını tek plot ta çizdirme
image=cv2.imread("hand.jpg")
for i,col in enumerate(["b","g","r"]):
    hist=cv2.calcHist([image],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
plt.show()