import numpy as np

user_input = input("Enter elements for the array (comma-separated): ")
array = np.array([int(elem) for elem in user_input.split(',')])

cumulative_sum_result = np.cumsum(array)

title = "Cumulative Sum | John Louie Ubias | 3 BSIT-2"
print(cumulative_sum_result)
print(title)

