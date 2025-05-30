# Split the array in 3 parts
import numpy as np

user_input = input("Enter elements for the array (comma-separated): ")
arr = np.array([int(x) for x in user_input.split(',')])

num_parts = int(input("Enter the number of parts to split the array into: "))
newarr = np.array_split(arr, num_parts)

title = "Split the array in 3 parts | John Louie Ubias | 3 BSIT-2"
print(newarr)
print(title)