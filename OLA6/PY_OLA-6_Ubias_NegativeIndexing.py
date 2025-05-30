import numpy as np

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
arr = np.zeros((rows, cols), dtype=int)

for i in range(rows):
    user_input = input(f"Enter elements for row {i + 1} (comma-separated): ")
    arr[i] = [int(x) for x in user_input.split(',')]
title = "Negative Indexing | John Louie Ubias | 3 BSIT-2"

print('Last element from 2nd dim:', arr[1, -1])
print(title)