import numpy as np

user_input = input("Enter elements for the array (comma-separated): ")
arr = np.array([int(x) for x in user_input.split(',')])

search_value = int(input("Enter the value to search for: "))
x = np.where(arr == search_value)

title = "NumPy Searching Arrays | John Louie Ubias | 3 BSIT-2"
print(x)
print(title)