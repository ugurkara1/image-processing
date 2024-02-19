import cv2
import numpy as np

def label_connected_components(image):
    _, labeled_image = cv2.connectedComponents(image)
    return labeled_image

def main():
    # Renkli görüntüyü oku
    original_image = cv2.imread('goruntu.jpg')

    if original_image is None:
        print("Görüntü yüklenemedi. Dosya adını ve yolunu kontrol edin.")
        return

    # Görüntüyü gri seviyeye dönüştür
    gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

    # Gri seviyeli görüntü üzerinde eşikleme yaparak ikili bir görüntü elde et
    _, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

    # Bağlantılı bileşenleri etiketle
    labeled_image = label_connected_components(binary_image)

    # Görüntüleri ekranda göster
    cv2.imshow('Original Image', original_image)
    cv2.imshow('Gray Image', gray_image)
    cv2.imshow('Binary Image', binary_image)
    cv2.imshow('Labeled Image', np.uint8(labeled_image))

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()