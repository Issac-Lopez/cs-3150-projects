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
# (4) Median Filter
height,width = np.shape(img)
median = np.zeros((height,width),dtype=float)
for i in range(1,height-2):
    for j in range(1,width-2):
        sorted_pixels = sorted(np.ndarray.flatten(img[i-1:i+2,j-1:j+2]))
        median[i][j] = sorted_pixels[4]
plt.figure(figsize=(7,7))
# Original
plt.subplot(1,2,1), plt.imshow(img, cmap='gray', vmin=0, vmax=255), plt.title('Original')
plt.xticks([]), plt.yticks([])
# Median
plt.subplot(1,2,2), plt.imshow(median, cmap='gray', vmin=0, vmax=255), plt.title('Median Filter')
plt.xticks([]), plt.yticks([])
