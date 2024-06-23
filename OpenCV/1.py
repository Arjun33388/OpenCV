import cv2

img = cv2.imread('C:/Users/arjun/OneDrive/Desktop/OpenCV/assets/Portfolio-header.png',1)
img = cv2.resize(img, (1000,250))

cv2.imwrite('new_img.jpg',img)
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()