
# Goruntu isleme 2022-2023 odev 1
# Selami Caliskan
# 02210201505 Bilgisayar Muhendisligi 3. Sınıf Orgun

import cv2
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

image=cv2.imread("yozgat.jpg", 0)

def calculateHistogram(image, plot=True):
    """
    This function used to calculate the histogram density of single-channel images and plot the graph.

    :param image: input image (np.array)
    :param plot: plot histogram graph (boolean)
    :return: historam density (tuple)
    """

    hist=np.zeros(256, dtype=int)
    (w, h)=image.shape

    for v in range(w):
        for u in range(h):
            i=image[v, u]
            hist[i]=hist[i]+1

    if plot:
        plt.bar(np.arange(0, 256, 1), hist, color="g")
        plt.show()
    return (hist)

values=calculateHistogram(image, True) # call the function

counter = dict(map(lambda i, j: (i, j), np.arange(0, 256, 1), values))
print(counter)

# Additional!
# Plot histogram graph with matlplotlib library
plt.hist(image.ravel(), 256, [0, 256], color="r")
plt.show()

