# Addition
import numpy as np

user_input1 = input("Enter elements for the first array (comma-separated): ")
user_input2 = input("Enter elements for the second array (comma-separated): ")

arr1 = np.array([int(elem) for elem in user_input1.split(',')])
arr2 = np.array([int(elem) for elem in user_input2.split(',')])

newarr = np.add(arr1, arr2)

title = "Addition | John Louie Ubias | 3 BSIT-2"
print(newarr)
print(title)