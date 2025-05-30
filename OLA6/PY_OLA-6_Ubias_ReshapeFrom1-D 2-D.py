import numpy as np

user_input = input("Enter elements for the array (comma-separated): ")
arr = np.array([int(x) for x in user_input.split(',')])

title = "Reshape From 1-D to 2-D | John Louie Ubias | 3 BSIT-2"
newarr = arr.reshape(4, 3)

print(newarr)
print(title)