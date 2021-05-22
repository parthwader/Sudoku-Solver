# Sudoku-Solver
Given an image of a sudoku grid, it performs following steps:

1. Gaussian Blur to remove noise
2. Canny edge detection using Otsu threshold values
3. Extraction of largest contour
3. Perspective transform (homography) to get top view
4. Adaptive thresholding to get binary image
5. Extraction of each cell of 9x9 grid
6. Using KNN to perform OCR
7. Solving the sudoku using recursion and backtracking

Note: A gif is included showing the working of the project
