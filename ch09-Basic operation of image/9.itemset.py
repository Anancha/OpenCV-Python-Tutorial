# -*- coding: utf-8 -*-
import cv2
import numpy as np

img = cv2.imread('data/messi5.jpg')

#
px = img[100, 100]
print(px)
blue = img[100, 100, 0]
print(blue)

#
img[100, 100] = [255, 255, 255]
print(img[100, 100])

# A better way to get pixel values and modify them. 

print(img.item(10, 10, 2))
img.itemset((10, 10, 2), 100)
print(img.item(10, 10, 2))
