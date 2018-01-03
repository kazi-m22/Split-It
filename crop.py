import os
import matplotlib
import cv2
import numpy as np


base = os.getcwd()
im_loc = base + '\\images'
images = os.listdir(base + '\\images')
im = []
n = 1
for i in images:
    im.append(im_loc+'\\'+i)
images = im
print(images)
for img in images:
    i = cv2.imread(img,0)
    # i = cv2.cvtColor(i, cv2.COLOR_BAYER_BG2GRAY)
    # ret, i = cv2.threshold(i, 180, 255, cv2.THRESH_BINARY)
    cv2.imwrite('%d'%n+'.jpg', i)
    n+=1

