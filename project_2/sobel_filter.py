from google.colab import drive
drive.mount('/content/drive')

!mkdir test
!mkdir mydata
!cp -r /content/drive/MyDrive/ImageData/portrait_512x512.jpg /content/mydata

import numpy as np
import cv2 
import math
import random
from matplotlib import pyplot as plt
from scipy.signal import convolve2d
# (0)   Load Image
im = cv2.imread('/content/mydata/portrait_512x512.jpg')

# (2) sobel filter by convolve 2d
sobel_vert = np.array([
         [-1.0, 0.0, 1.0]
        ,[-2.0, 0.0, 2.0]
        ,[-1.0, 0.0, 1.0]
        ])
sobel_horiz = sobel_vert.T
d_horiz = convolve2d(img, sobel_horiz, mode='same', boundary = 'symm', fillvalue=0)
d_vert = convolve2d(img, sobel_vert, mode='same', boundary = 'symm', fillvalue=0)
grad=np.sqrt(np.square(d_horiz) + np.square(d_vert))
grad *= 255.0 / np.max(grad)
plt.figure(figsize=(7,7))
# original
plt.subplot(2,2,1), plt.imshow(img, cmap='gray', vmin=0, vmax=255), plt.title('Original')
plt.xticks([]), plt.yticks([])
# Vert_by 2d Convolve
plt.subplot(2,2,2), plt.imshow(d_vert, cmap='gray', vmin=0, vmax=255), plt.title('Vert_by 2d Convolve')
plt.xticks([]), plt.yticks([])
# 'Horiz_ by 2d Convolve
plt.subplot(2,2,3), plt.imshow(d_horiz, cmap='gray', vmin=0, vmax=255), plt.title('Horiz_ by 2d Convolve')
plt.xticks([]), plt.yticks([])
# Gradient Edge
plt.subplot(2,2,4), plt.imshow(grad, cmap='gray', vmin=0, vmax=255), plt.title('Gradient Edge by 2d Conv')
plt.xticks([]), plt.yticks([])
