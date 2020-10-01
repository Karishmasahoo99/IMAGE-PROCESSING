import cv2
img= cv2.imread('./download.jpeg')
img1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img2=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img3=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('original_image',img)
cv2.imshow('RGB_image',img)
cv2.imshow('Gray_image',img2)
cv2.imshow('Hsv_image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
