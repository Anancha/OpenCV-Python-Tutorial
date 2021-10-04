# Update and review by Anucha Ananbenjappon

# -*- coding: utf-8 -*-

import numpy as np
import cv2

print(cv2.__version__)


img = cv2.imread('data/messi5.jpg',cv2.IMREAD_COLOR) #Read in a color image. The transparency of the image will be ignored. Default parameters. 
#img = cv2.imread('data/messi5.jpg', cv2.IMREAD_GRAYSCALE)# Load an color image in grayscale 灰度
#img = cv2.imread('data/messi5.jpg',cv2.IMREAD_UNCHANGED) # Load an color image in grayscale 灰度

img = cv2.resize(img, (640, 480))

# img.I
# AttributeError: 'numpy.ndarray' object has no attribute 'I'

#
rows,cols,ch=img.shape
print('Row/High:',rows,'Column/wide:',cols,'channel:',ch)
#The width of the image corresponds to the number of columns, and the height corresponds to the number of rows.

cv2.namedWindow('image', cv2.WINDOW_NORMAL)#可以调整窗口大小
# cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)#自动调整
# cv2.namedWindow('image', cv2.WINDOW_KEEPRATIO)#保持图片比例

# cv2.resizeWindow('image', 200, 200)  # 不起作用？

cv2.imshow('image', img)#窗口会自动调整为图像大小
# 在窗口上按任意键退出
cv2.waitKey(delay=0)#返回按键的 ASCII 码值

cv2.destroyAllWindows()

#
# cv2.imwrite('messigray.png', img)
