import numpy as np
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
arr = np.zeros((rows, cols), dtype=int)

for i in range(rows):
    user_input = input(f"Enter elements for row {i + 1} ({cols} elements, comma-separated): ")
    arr[i] = [int(x) for x in user_input.split(',')]
title = "Access 2-D Arrays | John Louie Ubias | 3 BSIT-2"

print('2nd element on 1st row: ', arr[0, 1])
print(title)