Note: A gif is included showing the working of the project

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

# TO-DO
1. Add the functionality of generating a Sudoku
2. Add the option to try out various methods to solve the Sudoku
  1. Dancing Links
  2. Spiral Backtracking 
  3. Reverese Backtracking
