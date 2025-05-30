import numpy as np

user_input = input("Enter elements for the array (comma-separated): ")
arr = np.array([int(x) for x in user_input.split(',')])

filter_values = input("Enter True/False values for filtering (comma-separated): ").lower().split(',')
filter_mask = [True if value == 'true' else False for value in filter_values]

newarr = arr[filter_mask]

title = "NumPy Filter Array | John Louie Ubias | 3 BSIT-2"
print(newarr)
print(title)