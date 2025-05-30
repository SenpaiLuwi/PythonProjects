import numpy as np

user_input = input("Enter elements for the array (comma-separated): ")
arr = np.array([x.strip() for x in user_input.split(',')])

title = "Checking Data Types B | John Louie Ubias | 3 BSIT-2"
print(arr.dtype)
print(title)