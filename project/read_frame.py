#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import numpy as np

def find_cross_points(x_coords, y_coords):
    
   # Find the cross points in the table by filtering out points that are too close to each other.
    
    x_coords = np.sort(x_coords)
    y_coords = np.sort(y_coords)

    filtered_x = [x_coords[0]]
    filtered_y = [y_coords[0]]

    for i in range(1, len(x_coords)):
        if x_coords[i] - x_coords[i - 1] > 10:
            filtered_x.append(x_coords[i])

    for j in range(1, len(y_coords)):
        if y_coords[j] - y_coords[j - 1] > 10:
            filtered_y.append(y_coords[j])

    return filtered_x, filtered_y

def has_content(image_section):
    
    #Determine if the given image section is non-empty.

    return np.any(image_section > 0)

def extract_table_structure(image_path):
    
   # Extract the structure of a table from an image and return a matrix indicating empty and filled cells, ignoring the first row and first column.
    
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise ValueError("Image not found or unable to load.")

    # Invert colors and apply adaptive threshold
    binary_image = cv2.adaptiveThreshold(~image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, -5)

    # Detect horizontal and vertical lines
    horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (binary_image.shape[1] // 20, 1))
    vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, binary_image.shape[0] // 10))

    horizontal_lines = cv2.dilate(cv2.erode(binary_image, horizontal_kernel), horizontal_kernel)
    vertical_lines = cv2.dilate(cv2.erode(binary_image, vertical_kernel), vertical_kernel)

    # Find intersections of horizontal and vertical lines
    intersections = cv2.bitwise_and(horizontal_lines, vertical_lines)

    # Extract table contents
    table_structure = cv2.add(horizontal_lines, vertical_lines)
    table_contents = cv2.subtract(binary_image, table_structure)

    # Locate intersection points
    y_coords, x_coords = np.where(intersections > 0)
    x_points, y_points = find_cross_points(x_coords, y_coords)

    # Create a matrix to represent the table cells, ignoring the first row and first column
    table_matrix = np.zeros((len(y_points) - 2, len(x_points) - 2), dtype=int)

    for i in range(1, len(x_points) - 1):
        for j in range(1, len(y_points) - 1):
            x_start, x_end = x_points[i], x_points[i + 1]
            y_start, y_end = y_points[j], y_points[j + 1]
            cell_contents = table_contents[y_start:y_end, x_start:x_end]
            if has_content(cell_contents):
                table_matrix[j - 1, i - 1] = 1

    return table_matrix

