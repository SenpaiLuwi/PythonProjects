import numpy as np

user_input = input("Enter elements for the array (comma-separated): ")
arr = np.array([int(x) for x in user_input.split(',')])

start_index = int(input("Enter the start index for slicing (inclusive): "))
sliced_array = arr[start_index:]
title = "Slicing Arrays B | John Louie Ubias | 3 BSIT-2"

print("Sliced array:", sliced_array)
print(title)