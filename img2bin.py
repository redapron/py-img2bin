import cv2
import numpy as np
import sys

n = sys.argv[1]
img_c =cv2.imread(n)
img = cv2.imread(n, cv2.IMREAD_GRAYSCALE)
(thresh, img) = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

height, width, channels = img_c.shape

print width, height
for i in range(height):
    for k in range(width):
        if img[i,k] == 255:
            p = '1'
        else:
            p = '0'

        if k != width - 1:
            p += ' '
        sys.stdout.write(p)
        sys.stdout.flush()

    print ''
