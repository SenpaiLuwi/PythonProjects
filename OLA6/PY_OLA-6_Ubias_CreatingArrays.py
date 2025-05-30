import numpy as np
user_input = input("Enter elements for the array (comma-separated): ")
arr = np.array([int(x) for x in user_input.split(',')])
title = "Creating Arrays | John Louie Ubias | 3 BSIT-2"

print("Array:", arr)
print("Type of array:", type(arr))
print(title)