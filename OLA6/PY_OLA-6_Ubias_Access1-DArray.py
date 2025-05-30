import numpy as np

user_input = input("Enter elements for the array (comma-separated): ")
arr = np.array([int(x) for x in user_input.split(',')])
title = "Access 1-D Array | John Louie Ubias | 3 BSIT-2"

print("Element at index 0:", arr[0])
print("Sum of elements at index 2 and 3:", arr[2] + arr[3])
print(title)
