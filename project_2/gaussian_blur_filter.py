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
# (5) Gaussian Filter
G_ker=np.array([
       [ 4,  6, 11, 6,  4],
       [10, 12, 17, 12, 10],
       [20, 24, 27, 24, 20],
       [29, 31, 36, 31, 29],
       [35, 37, 42, 37, 35]])
G_ker =G_ker/np.sum(G_ker)
Gaussian = cv2.filter2D(img, -1, G_ker) 
plt.figure(figsize=(12,12)) # x+5 and y+5 in comparison to the pervious usages
# Original
plt.subplot(1,3,1), plt.imshow(img, cmap='gray', vmin=0, vmax=255), plt.title('Original')
plt.xticks([]), plt.yticks([])
# Gaussian
plt.subplot(1,3,2), plt.imshow(Gaussian, cmap='gray', vmin=0, vmax=255), plt.title('Gaussian Blur')
plt.xticks([]), plt.yticks([])
