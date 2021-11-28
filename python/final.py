from scanner import scanner
from solver import sudoku

scan = scanner(r"C:\Users\Vikas Sharma\IdeaProjects\sudoku-solver\python_without_gui\Pics\Test_data\10.jpg")
scan.getDigits()

grid = scan.grid
unsolvedgrid=grid;
unsolvedgrid.tostring()
print(" The 9 x 9 matrix extracted from the image is : ")
print(unsolvedgrid)
print()
slv = sudoku(grid)

ifSolved = slv.solve()

if ifSolved == True:
    print("After solving the sudoku is :")
    print()
    slv.show()
else:
    print("Couldn't Solve")

# C:\Users\Vikas Sharma\IdeaProjects\sudoku-solver\python_without_gui\Pics\Train_data
