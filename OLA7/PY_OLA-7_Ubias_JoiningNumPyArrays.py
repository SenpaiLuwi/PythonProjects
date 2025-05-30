# Joining NumPy Arrays
import numpy as np

user_input1 = input("Enter elements for the first array (comma-separated): ")
user_input2 = input("Enter elements for the second array (comma-separated): ")

arr1 = np.array([int(x) for x in user_input1.split(',')])
arr2 = np.array([int(x) for x in user_input2.split(',')])

arr = np.concatenate((arr1, arr2))

title = "Joining NumPy Arrays | John Louie Ubias | 3 BSIT-2"
print(arr)
print(title)