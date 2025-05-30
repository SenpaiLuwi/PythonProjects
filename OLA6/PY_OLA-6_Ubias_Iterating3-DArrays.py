import numpy as np

depth = int(input("Enter the number of matrices: "))
rows = int(input("Enter the number of rows in each matrix: "))
cols = int(input("Enter the number of columns in each matrix: "))

arr = np.zeros((depth, rows, cols), dtype=int)

title = "Iterating 3-D Arrays | John Louie Ubias | 3 BSIT-2"
for x in arr:
    print(x)
for x in arr:
    for y in x:
        for z in y:
            print(z)
print(title)