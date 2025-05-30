# Join two 2-D arrays along rows (axis=1)
import numpy as np

rows = int(input("Enter the number of rows for the arrays: "))
cols = int(input("Enter the number of columns for the arrays: "))

user_input1 = input("Enter elements for the first array (comma-separated): ")
user_input2 = input("Enter elements for the second array (comma-separated): ")

arr1 = np.array([int(x) for x in user_input1.split(',')]).reshape(rows, cols)
arr2 = np.array([int(x) for x in user_input2.split(',')]).reshape(rows, cols)

arr = np.concatenate((arr1, arr2), axis=1)

title = "Join two 2-D arrays along rows (axis=1) | John Louie Ubias | 3 BSIT-2"
print(arr)
print(title)