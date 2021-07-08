# -*- coding: utf-8 -*-
import cv2
import numpy as np

'''
For example, to detect the position of the eyes in an image,
we should first find the face in the image and then find the eyes in the area of the face.
Instead of searching directly in an image. This will improve the accuracy and performance of the program.
'''

img=cv2.imread('../data/messi5.jpg')

ball=img[280:340,330:390]
img[273:333,100:160]=ball #修改像素值



cv2.namedWindow("messi",0)
cv2.imshow("messi",img)
cv2.waitKey(0)
