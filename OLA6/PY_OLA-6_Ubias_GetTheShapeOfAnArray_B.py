import numpy as np

user_input = input("Enter elements for the array (comma-separated): ")
arr = np.array([int(x) for x in user_input.split(',')], ndmin=5)

title = "Get the Shape of an Array B | John Louie Ubias | 3 BSIT-2"
print(arr)
print('shape of array:', arr.shape)
print(title)
