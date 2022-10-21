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
# (3) Laplacian
l_kern = np.array([
         [1.0,  1.0, 1.0]
        ,[1.0, -8.0, 1.0]
        ,[1.0,  1.0, 1.0]
        ])

Edge_l = cv2.filter2D(img, -1, l_kern)
plt.figure(figsize=(7,7))
# Original image
plt.subplot(1,2,1), plt.imshow(img, cmap='gray', vmin=0, vmax=255), plt.title('Original')
plt.xticks([]), plt.yticks([])
# Laplacian
plt.subplot(1,2,2), plt.imshow(Edge_l, cmap='gray', vmin=0, vmax=255), plt.title('Laplacian Edge')
plt.xticks([]), plt.yticks([])
