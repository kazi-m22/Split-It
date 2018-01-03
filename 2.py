from matplotlib import pyplot as plt
import cv2
import numpy as np
from PIL import Image
import os

temp = plt.imread('1.png')
i_h, i_w= temp.shape
temp = temp[0:i_h, 10:i_w]
h,w= temp.shape
print(temp.shape)

location  = os.getcwd()
  

x = 0
y = 0
n=0

if(h<950) | (h<698):
    print('invalid image')
else:
    part_y = h/4
    part_x = w/3
    
    while y<h:    

        while x< w:
            if(os.path.exists('photos')):
                os.chdir(location + '/photos')
                print(part_y)
                print(type(part_x))
                img_1 = temp[int(y) :int(part_y), int(x):int(part_x)]
                x = part_x
                part_x = part_x + part_x
                
                plt.imshow(img_1, cmap = 'gray')
                plt.show()
                plt.imsave('img' + str(n), img_1,  cmap = 'gray')
                n = n+1
                
            else:
                os.mkdir('photos')
                continue

        x = 0    
        part_x = w/3
        y = part_y
        y = part_y
        part_y = part_y +(h/4)
        

        
    
plt.show()
