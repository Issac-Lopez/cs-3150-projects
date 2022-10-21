!mkdir test
!mkdir mydata
!cp -r /content/drive/MyDrive/ImageData/portrait.jpg /content/mydata
import numpy as np
import cv2 
import math
import random
from matplotlib import pyplot as plt

im = cv2.imread('/content/mydata/portrait.jpg')
#print(im)
img = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY) # needed for opencv on colab
length, width = img.shape # used to add circle
imgN = img / 255 # gamma/power law
img = imgN**0.65 # gamma/power law
plt.figure()

radius = .45 * min(length,width)

for i in range(length):     # this is the row
    for j in range(width):  # this is the column      
        if math.sqrt((i - length / 2)**2 + (j - width / 2)**2) > radius: # < radius makes image be outside of circle
          img[i,j] = 255

plt.figure()
plt.axis('off') # hides the axes for graph
plt.imshow(img, cmap = 'gray', vmin = 0, vmax = 1)
