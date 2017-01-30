
from matplotlib import pyplot as plt
import numpy as np
import cv2
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])
img = cv2.imread('1.jpg')

img = rgb2gray(img)

plt.imshow(img1)
plt.show()


