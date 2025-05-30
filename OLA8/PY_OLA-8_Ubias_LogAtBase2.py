# Log at Base 2
import numpy as np

user_input = input("Enter elements for the array (comma-separated): ")

arr = np.array([int(elem) for elem in user_input.split(',')])

title = "Log at Base 2 | John Louie Ubias | 3 BSIT-2"
print(np.log2(arr))
print(title)