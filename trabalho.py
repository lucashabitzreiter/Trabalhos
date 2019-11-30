import numpy as np
from matplotlib import pyplot as plt
import cv2
img = cv2.imread("lucas_color.png", cv2.IMREAD_COLOR)
blur = cv2.blur(img,(5,5))
    
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()
   

