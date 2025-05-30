import numpy as np

depth = int(input("Enter the number of matrices: "))
rows = int(input("Enter the number of rows in each matrix: "))
cols = int(input("Enter the number of columns in each matrix: "))

arr = np.zeros((depth, rows, cols), dtype=int)

title = "Iterating Arrays Using nditer() | John Louie Ubias | 3 BSIT-2"
for x in np.nditer(arr):
    print(x)
print(title)