import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('data/messi5.jpg', 0)
plt.imshow(img, cmap='gray', interpolation='bicubic')
# The color image is loaded in BGR mode when using OpenCV. But Matplotlib is in RGB mode. So if the color image has been read by OpenCV, it will not be displayed correctly by Matplotlib.

plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
