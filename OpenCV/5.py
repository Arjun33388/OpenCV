import cv2
import numpy as np

img = cv2.imread('assets/chessboard.png')

cv2.imshow('frame',img)
cv2.waitKey(0)
cv2.destroyAllWindows()