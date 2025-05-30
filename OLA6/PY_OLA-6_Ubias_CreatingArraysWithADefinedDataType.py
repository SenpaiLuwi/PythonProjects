import numpy as np

user_input = input("Enter elements for the array (comma-separated): ")
data_type_input = input("Enter the desired data type (e.g., 'S' for string, 'i4' for int32): ")
arr = np.array([x.strip() for x in user_input.split(',')], dtype=data_type_input)
title = "Creating Arrays With a Defined Data Type | John Louie Ubias | 3 BSIT-2"

print(arr)
print(arr.dtype)
print(title)
