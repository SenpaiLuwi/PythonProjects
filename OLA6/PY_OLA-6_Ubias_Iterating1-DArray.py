import numpy as np

user_input = input("Enter elements for the array (comma-separated): ")
arr = np.array([int(x) for x in user_input.split(',')])

title = "Iterating 1-D Array | John Louie Ubias | 3 BSIT-2"
for x in arr:
    print(x)
print(title)