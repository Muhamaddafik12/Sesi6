import numpy as np
import imageio as img
import matplotlib.pyplot as plt

path = 'C:\Users\KOMPUTER  JARKOM 21\Pictures\anazz\sesi5\download (1).jpeg'
image = img.imread(path)

height, width = image.shape[:2]
mirrored = np.zeros_like(image)

# Flip both horizontally and vertically at the same time
for y in range(height):
    for x in range(width):
        mirrored[y, x] = image[height - 1 - y, width - 1 - x]

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title("Original")

plt.subplot(1, 2, 2)
plt.imshow(mirrored)
plt.title("Horizontal & Vertical Flip")

plt.show()
