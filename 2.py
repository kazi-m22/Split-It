from matplotlib import pyplot as plt
import cv2
img = plt.imread('1.png')


h,w = img.shape

print('w ',w, ' ', 'h ', h)   

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
            img_1 = img[y :part_y, x:part_x]
            x = part_x
            part_x = part_x + part_x
            
            plt.imshow(img_1)
            plt.show()

        x = 0    
        part_x = w//3
        y = part_y
        part_y = part_y +part_y

    
plt.show()
