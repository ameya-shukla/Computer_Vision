#import the OpenCV library
import cv2

#reading the file through the path
path = r"/Users/ameyashukla/Ameya Shukla Personal/Ameya/Ameya.jpg"

image = cv2.imread(path)

#Converting the image to Grayscale
gray_img = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

#Converting the grayscale image to binary image
ret, binary_image = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)


cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray_img)
cv2.imshow("Binary Image", binary_image)

cv2.waitKey(0)
