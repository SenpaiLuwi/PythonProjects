import numpy as np

user_input = input("Enter elements for the array (comma-separated): ")
arr = np.array([int(x) for x in user_input.split(',')])

title = "Checking Data Types A | John Louie Ubias | 3 BSIT-2"
print(arr.dtype)
print(title)
