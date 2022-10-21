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
# (1) Average(Mean) Filter
img = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
box = np.array(
    [[0.04, 0.04, 0.04, 0.04, 0.04],
    [0.04, 0.04, 0.04, 0.04, 0.04],
    [0.04, 0.04, 0.04, 0.04, 0.04],
    [0.04, 0.04, 0.04, 0.04, 0.04],
    [0.04, 0.04, 0.04, 0.04, 0.04]]
) 
box2 = np.array(
    [[1/9,1/9,1/9],
    [1/9,1/9,1/9],
    [1/9,1/9,1/9]]
)
average = cv2.filter2D(img,-1,box)
plt.figure(figsize=(7,7))
# original
plt.subplot(1,2,1), plt.imshow(img, cmap='gray', vmin=0, vmax=255), plt.title('Original')
plt.xticks([]), plt.yticks([])
# average
plt.subplot(1,2,2), plt.imshow(average, cmap='gray', vmin=0, vmax=255), plt.title('Average Filter')
plt.xticks([]), plt.yticks([])
plt.show()
