import numpy as np

user_input = input("Enter elements for the array (comma-separated): ")
arr = np.array([int(x) for x in user_input.split(',')])

end_index = int(input("Enter the end index for slicing (exclusive): "))
sliced_array = arr[:end_index]
title = "Slicing Arrays C | John Louie Ubias | 3 BSIT-2"

print("Sliced array:", sliced_array)
print(title)
