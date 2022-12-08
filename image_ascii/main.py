import cv2
import numpy as np

CHAR_LIST = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

image = cv2.imread("input.jpg", 0)
num_cols = 200
# print(image)
height, width = image.shape
cell_width = width / num_cols
cell_height = cell_width *2
num_rows = int(height / cell_height)
output_file = open("image.txt", "w")
for i in range(num_rows):
    for j in range(num_cols):
        sub_image = image[int(i*cell_height):int((i+1)*cell_height), int(j*cell_width): int((j+1)*cell_width)] 
        index = int(np.mean(sub_image)/255*len(CHAR_LIST))
        output_file.write(CHAR_LIST[index])
    output_file.write("\n")
output_file.close()    