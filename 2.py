from matplotlib import pyplot as plt
import cv2
import numpy as np
from PIL import Image


fname = '1.png'

img = Image.open(fname).convert("L")
temp = np.asarray(img)
i_h, i_w = temp.shape
temp = temp[0:i_h, 10:i_w]
h,w = temp.shape

  

x = 0
y = 0
n=1

if(h<950) | (h<698):
    print('invalid image')
else:
    part_y = h//4
    part_x = w//3
    
    while y<h:    

        while x<= w:
            img_1 = temp[y :part_y, x:part_x]
            x = part_x
            part_x = part_x + part_x
            
            plt.imshow(img_1, cmap = 'gray')
            plt.show()

        x = 0    
        part_x = w//3
        y = part_y
        y = part_y
        part_y = part_y +(h//4)
        

    
plt.show()
