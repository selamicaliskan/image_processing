

# Selami Çalışkan Goruntu isleme odev 2
# 02210201505 Bilgisayar Muhendisligi 3. sınıf orgun


import cv2
import matplotlib.pyplot as plt

img=cv2.imread("yozgat.jpg",0)

def find_max(matrix):
    largest=0
    h,w=matrix.shape
    for i in range(h):
        for j in range(w):
            if img[i][j]>largest:
                largest=img[i][j]
    return largest

def invert_image(image):
    return find_max(image)-image


_, ax = plt.subplots(2)
ax[0].imshow(img,cmap="gray")
ax[1].imshow(invert_image(img),cmap="gray")
plt.show()
