# Joining NumPy Arrays
# import numpy as np
#
# user_input1 = input("Enter elements for the first array (comma-separated): ")
# user_input2 = input("Enter elements for the second array (comma-separated): ")
#
# arr1 = np.array([int(x) for x in user_input1.split(',')])
# arr2 = np.array([int(x) for x in user_input2.split(',')])
#
# arr = np.concatenate((arr1, arr2))
#
# title = "Joining NumPy Arrays | John Louie Ubias | 3 BSIT-2"
# print(arr)
# print(title)

# Join two 2-D arrays along rows (axis=1)
# import numpy as np
#
# rows = int(input("Enter the number of rows for the arrays: "))
# cols = int(input("Enter the number of columns for the arrays: "))
#
# user_input1 = input("Enter elements for the first array (comma-separated): ")
# user_input2 = input("Enter elements for the second array (comma-separated): ")
#
# arr1 = np.array([int(x) for x in user_input1.split(',')]).reshape(rows, cols)
# arr2 = np.array([int(x) for x in user_input2.split(',')]).reshape(rows, cols)
#
# arr = np.concatenate((arr1, arr2), axis=1)
#
# title = "Join two 2-D arrays along rows (axis=1) | John Louie Ubias | 3 BSIT-2"
# print(arr)
# print(title)

# Split the array in 3 parts
# import numpy as np
#
# user_input = input("Enter elements for the array (comma-separated): ")
# arr = np.array([int(x) for x in user_input.split(',')])
#
# num_parts = int(input("Enter the number of parts to split the array into: "))
# newarr = np.array_split(arr, num_parts)
#
# title = "Split the array in 3 parts | John Louie Ubias | 3 BSIT-2"
# print(newarr)
# print(title)

# NumPy Searching Arrays
# import numpy as np
#
# user_input = input("Enter elements for the array (comma-separated): ")
# arr = np.array([int(x) for x in user_input.split(',')])
#
# search_value = int(input("Enter the value to search for: "))
# x = np.where(arr == search_value)
#
# title = "NumPy Searching Arrays | John Louie Ubias | 3 BSIT-2"
# print(x)
# print(title)

# NumPy Sorting Arrays
# import numpy as np
#
# user_input = input("Enter elements for the array (comma-separated): ")
# arr = np.array([x.strip() for x in user_input.split(',')])
#
# title = "NumPy Sorting Arrays | John Louie Ubias | 3 BSIT-2"
# print(np.sort(arr))
# print(title)

# NumPy Filter Array
# import numpy as np
#
# user_input = input("Enter elements for the array (comma-separated): ")
# arr = np.array([int(x) for x in user_input.split(',')])
#
# filter_values = input("Enter True/False values for filtering (comma-separated): ").lower().split(',')
# filter_mask = [True if value == 'true' else False for value in filter_values]
#
# newarr = arr[filter_mask]
#
# title = "NumPy Filter Array | John Louie Ubias | 3 BSIT-2"
# print(newarr)
# print(title)
































































































































