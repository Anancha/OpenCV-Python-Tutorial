import numpy as np
import cv2


img = cv2.imread('data/messi5.jpg', 0)   #Edit path from missi5.jpg to data/missi5.jpg
img = cv2.imread('data/messi5.jpg', 0)  # edit by Anucha from messi5.jpg to data/messi5.jpg 

cv2.imshow('image', img)

k = cv2.waitKey(0)
if k == 27:  # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'):  # wait for 's' key to save and exit
    cv2.imwrite('messigray.png', img)
    cv2.destroyAllWindows()
