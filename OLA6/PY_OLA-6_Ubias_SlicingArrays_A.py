import numpy as np

user_input = input("Enter elements for the array (comma-separated): ")
arr = np.array([int(x) for x in user_input.split(',')])
title = "Slicing Arrays A | John Louie Ubias | 3 BSIT-2"

start_index = int(input("Enter the start index for slicing: "))
end_index = int(input("Enter the end index for slicing: "))
print("Sliced array:", arr[start_index:end_index])
print(title)
