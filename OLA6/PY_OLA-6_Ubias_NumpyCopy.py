import numpy as np

user_input = input("Enter elements for the array (comma-separated): ")
arr = np.array([int(x) for x in user_input.split(',')])
title = "Numpy Copy | John Louie Ubias | 3 BSIT-2"
x = arr.copy()
arr[0] = 42

print(arr)
print(x)
print(title)