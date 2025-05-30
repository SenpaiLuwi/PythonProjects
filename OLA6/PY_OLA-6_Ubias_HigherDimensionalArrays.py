import numpy as np

user_input = input("Enter elements for the array (comma-separated): ")
num_dimensions = int(input("Enter the number of dimensions: "))
arr = np.array([int(x) for x in user_input.split(',')], ndmin=num_dimensions)
title = "Higher Dimensional Arrays | John Louie Ubias | 3 BSIT-2"

print("Array:", arr)
print("Number of dimensions:", arr.ndim)
print(title)
