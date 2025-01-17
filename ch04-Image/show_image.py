# -*- coding: utf-8 -*-
# @Time    : 2018/1/19 20:39
# @Author  : play4fun
# @File    : show_image.py
# @Software: PyCharm

"""
show_image.py:
Make useful tools for daily use
Set in environment variables:
alias show='/Users/play/.py3/bin/python3.6 /Users/play/github/OpenCV-Python-Tutorial/ch04-图片/show_image.py '

"""

import numpy as np
import cv2, sys

if len(sys.argv) < 2:
    print('show_image.py image_path')
    sys.exit(0)

image_path = sys.argv[1]
try:
    f = open(image_path)
except Exception as e:
    print(e)
    sys.exit(-1)

img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED) # Include the alpha channel of the image
temp = img.copy()

title = image_path.split('/')[-1] + f' {img.shape}'

gray = False
while True:
    cv2.imshow(title, temp)

    k = cv2.waitKey(10)
    if k == 27 or k == ord('q'):
        break
    #TODO resolution is too large and needs to be scaled
    if k == ord('g'):
        # t = temp == img
        # if t.all():
        # if t.any():
        # if temp == img:
        if gray is False:
            temp = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            gray = True
        else:
            temp = img.copy()
            gray = False

cv2.destroyAllWindows()
