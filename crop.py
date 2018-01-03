import os
import matplotlib
import cv2
import numpy as np


base = os.getcwd()
im_loc = './images'
images = os.listdir(im_loc)
im = []
n = 1
for t in images:
    im.append(im_loc+'/'+t)
images = im
print(images)
i=0
while i<len(images):

    img = cv2.imread(images[i])
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, img = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
    cv2.imwrite(images[i], img)
    i = i + 1
