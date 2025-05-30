import numpy as np

user_input = input("Enter elements for the array (comma-separated): ")
arr = np.array([int(x) for x in user_input.split(',')])

title = "Iterating Array With Different Data Types | John Louie Ubias | 3 BSIT-2"
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x)
print(title)