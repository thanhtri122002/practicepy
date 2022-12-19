import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Capture001.png')

kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])

image_sharp = cv2.filter2D(src=img, ddepth=-1, kernel=kernel)
cv2.imshow('sharped', image_sharp)
cv2.waitKey()
cv2.destroyAllWindows()