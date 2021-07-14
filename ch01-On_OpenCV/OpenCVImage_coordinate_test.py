# -*- coding: utf-8 -*-
# @Time    : 2017/7/28 23:13
# @Update  : 2021/7/14 by Anucha
# @Author  : play4fun
# @File    : OpenCVImage_coordinate_test.py
# @Software: PyCharm, VS Code

"""
OpenCVImage_coordinate_test.py:
"""

# TODO


import numpy as np
import cv2

img = cv2.imread('data/Lenna.png', cv2.IMREAD_UNCHANGED)
print('img.shape:', img.shape)
logo = cv2.imread('data/opencv_logo.png', cv2.IMREAD_UNCHANGED)
logo = cv2.resize(logo, (20, 20))
print('logo.shape:', logo.shape)
butterfly= cv2.imread('data/butterfly.jpg', cv2.IMREAD_UNCHANGED)
butterfly = cv2.resize(butterfly, (20, 20))
print('butterfly.shape:', butterfly.shape)


cv2.imshow('src', img)
cv2.moveWindow('src', 0, 0)

# read color values at position y, x
y = 100
x = 50
(b, g, r) = img[y, x]
# print color values to screen
print('bgr:',b,g,r)

#First row and then column
#img[y:y+height,x:width]
img[100:100 + logo.shape[0], 300:300 + logo.shape[1]] = logo[:, :, 0:3]# The shapes of the two pictures are different
# img[10:10+logo.shape[0],30:30+logo.shape[1],:]=logo[:,:,0:3]
img[300:300 + logo.shape[1], 100:100 + logo.shape[0]] = butterfly[:, :, 0:3]


font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, text='col=width=X0,row=height-Y0', org=(0, 0), fontFace=font, fontScale=0.5, color=(0, 255, 0), thickness=2,bottomLeftOrigin=True)  # text,
cv2.putText(img, text='col=width=X10,row=height-Y30', org=(10, 30), fontFace=font, fontScale=0.5, color=(0, 255, 0), thickness=2)  # text,
cv2.putText(img, text='col=width=X100,row=height-Y300', org=(100, 300), fontFace=font, fontScale=0.5, color=(0, 255, 0), thickness=2)  # text,
cv2.putText(img, text='col=width-X300,row=height-Y100', org=(300, 100), fontFace=font, fontScale=0.5, color=(0, 255, 0), thickness=2)  # text,

cv2.imshow('img+logo', img)
cv2.imwrite('img_logo.jpg',img)
cv2.moveWindow('img+logo', x=img.shape[0], y=0)
cv2.waitKey(0)
