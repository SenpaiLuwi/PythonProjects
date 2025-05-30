import numpy as np

depth = int(input("Enter the number of matrices: "))
rows = int(input("Enter the number of rows in each matrix: "))
cols = int(input("Enter the number of columns in each matrix: "))
arr = np.zeros((depth, rows, cols), dtype=int)

for d in range(depth):
    print(f"Matrix {d + 1}:")
    for i in range(rows):
        user_input = input(f"  Enter elements for row {i + 1} (comma-separated): ")
        arr[d, i] = [int(x) for x in user_input.split(',')]
title = "Access 3-D Arrays | John Louie Ubias | 3 BSIT-2"

print("Element at coordinates (0, 1, 2):", arr[0, 1, 2])
print(title)