# Addition Function
import numpy as np

user_input_x = input("Enter elements for the first list (comma-separated): ")
user_input_y = input("Enter elements for the second list (comma-separated): ")

x = np.array([int(elem) for elem in user_input_x.split(',')])
y = np.array([int(elem) for elem in user_input_y.split(',')])

myadd = np.frompyfunc(lambda a, b: a + b, 2, 1)

title = "Addition Function | John Louie Ubias | 3 BSIT-2"
print(myadd(x, y))
print(title)