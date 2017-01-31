from matplotlib import pyplot as plt
import cv2
img = plt.imread('1.png')


h,w = img.shape

  

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
            img_1 = cnv[y :part_y, x:part_x]
            x = part_x
            part_x = part_x + part_x
            
            plt.imshow(img_1)
            plt.show()

        x = 0    
        part_x = w//3
        y = part_y
        y = part_y
        part_y = part_y +(h//4)
        

    
plt.show()
