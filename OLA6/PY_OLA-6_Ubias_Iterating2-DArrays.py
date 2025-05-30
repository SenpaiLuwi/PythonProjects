import numpy as np

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

arr = np.zeros((rows, cols), dtype=int)

title = "Iterating 2-D Arrays | John Louie Ubias | 3 BSIT-2"
for x in arr:
    print(x)
print(title)