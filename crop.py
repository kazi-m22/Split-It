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

#thresholding images of a folder

while i<len(images):

    img = cv2.imread(images[i])
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, img = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
    cv2.imwrite(images[i], img)
    i = i + 1


for im in images:
    img = cv2.imread(im)
    h,w,c = img.shape
    img = img[200:h, 50:w]
    h,w,c = img.shape
    x = 0
    y = 0
    part_y = y/4
    part_x = w/4

    while y<h:
        while x<w:

            img_1 = img[int(y):int(part_y), int(x): int(part_x)]
            x = part_x
            part_x = part_x + part_x
            if img_1.shape[0] !=0:
                if os.path.exists('outputs'):
                    cv2.imwrite('./outputs/%d'%n+'.jpg', img_1)
                else:
                    os.mkdir('outputs')
                    cv2.imwrite('./outputs/%d'%n + '.jpg', img_1)
            n += 1
        x = 0
        part_x = w / 3
        y = part_y
        part_y = part_y + (h / 4)

