# Vectorization B
import numpy as np

user_input_x = input("Enter elements for the first list (comma-separated): ")
user_input_y = input("Enter elements for the second list (comma-separated): ")

x = np.array([int(elem) for elem in user_input_x.split(',')])
y = np.array([int(elem) for elem in user_input_y.split(',')])

z = np.add(x, y)

title = "Vectorization B | John Louie Ubias | 3 BSIT-2"
print(z)
print(title)