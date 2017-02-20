import cv2
import os
import numpy as np

print(os.getcwd())

location = "E:\\Projects\\python\\shahidul dataset\\2"  #path of that folder which contains pictures
os.chdir(location)

images = os.listdir()
length = len(images)

i = 0

while(i<length):
    img = cv2.imread(images[i])
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, img = cv2.threshold(img, 180, 255, cv2.THRESH_BINARY)
    cv2.imwrite(images[i], img)
    i = i+1



cv2.waitKey(0)
cv2.destroyAllWindows()
