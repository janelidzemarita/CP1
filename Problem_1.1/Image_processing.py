import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('Problem_1.1/image.jpg', cv2.IMREAD_COLOR)
image2 = cv2.imread('Problem_1.1/car.jpg', cv2.IMREAD_COLOR)
# Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(image, (5, 5), 0, 9)
blurred2 = cv2.GaussianBlur(image2, (5, 5), 0, 9)

# Perform Canny edge detection
edges = cv2.Canny(blurred, 100, 200)
edges2 = cv2.Canny(blurred2, 100, 200)

# Display the original image and the detected edges
plt.subplot(121), plt.imshow(image)
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edges, cmap='gist_yarg')
plt.title('Edge Detection'), plt.xticks([]), plt.yticks([])

plt.subplot(121), plt.imshow(image2)
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edges2, cmap='gray')
plt.title('Edge Detection'), plt.xticks([]), plt.yticks([])

plt.show()
