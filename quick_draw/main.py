import numpy as np
import cv2 

images = np.load("full_numpy_bitmap_apple.npy")
print(images.shape)
image =images[10100]
print(image)
image = np.reshape(image, (28,28))
cv2.imwrite("apple.jpg", image)