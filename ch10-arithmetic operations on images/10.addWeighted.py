# -*- coding: utf-8 -*-
import cv2
import numpy as np

# Learn arithmetic operations on images, addition, subtraction, bit operations, etc.

# You can use the function cv2.add() to add two images. Of course, you can also use numpy directly.
# res=img1+img
# The size and type of the two images must be the same, or the second image can be a simple scalar value. 


x = np.uint8([250])
y = np.uint8([10])
print(cv2.add(x, y))  # 250+10 = 260 => 255
# [[255]]
print(x + y)  # 250+10=260%256=4
# [4]


# 图像混合  # Image mixing 
img1 = cv2.imread('data/ml.png')
img2 = cv2.imread('data/opencv_logo.jpg')

dst = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)  # 第一幅图的权重是 0.7 第二幅图的权重是 0.3
 # The weight of the first image is 0.7 and the weight of the second image is 0.3 

cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
