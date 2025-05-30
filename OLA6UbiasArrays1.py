# Importing NumPy
# import numpy as np
#
# user_input = input("Enter elements for the array (comma-separated): ")
# arr = np.array([int(x) for x in user_input.split(',')])
# title = "\nImport NumPy as np | John Louie Ubias | 3 BSIT-2"
#
# print("Array:", arr)
# print(title)


# Creating Arrays
# import numpy as np
# user_input = input("Enter elements for the array (comma-separated): ")
# arr = np.array([int(x) for x in user_input.split(',')])
# title = "Creating Arrays | John Louie Ubias | 3 BSIT-2"
#
# print("Array:", arr)
# print("Type of array:", type(arr))
# print(title)

# Dimensions in Arrays
# import numpy as np
# input_a = input("Enter a single element for array 'a': ")
# a = np.array(int(input_a))
# input_b = input("Enter elements for array 'b' (comma-separated): ")
# b = np.array([int(x) for x in input_b.split(',')])
# input_c = input("Enter elements for a 2D array 'c' (comma-separated, rows separated by semicolon): ")
# c = np.array([list(map(int, row.split(','))) for row in input_c.split(';')])
# input_d = input("Enter elements for a 3D array 'd' (semicolon-separated, matrices separated by pipe): ")
# d = np.array([[[int(z) for z in item.split(',')] for item in row.split(';')] for row in input_d.split('|')])
# title = "Dimensions in Arrays | John Louie Ubias | 3 BSIT-2"
#
# print("Dimension of array 'a':", a.ndim)
# print("Dimension of array 'b':", b.ndim)
# print("Dimension of array 'c':", c.ndim)
# print("Dimension of array 'd':", d.ndim)
# print(title)

# Higher Dimensional Arrays
# import numpy as np
#
# user_input = input("Enter elements for the array (comma-separated): ")
# num_dimensions = int(input("Enter the number of dimensions: "))
# arr = np.array([int(x) for x in user_input.split(',')], ndmin=num_dimensions)
# title = "Higher Dimensional Arrays | John Louie Ubias | 3 BSIT-2"
#
# print("Array:", arr)
# print("Number of dimensions:", arr.ndim)
# print(title)

# Access 1-D Array
# import numpy as np
#
# user_input = input("Enter elements for the array (comma-separated): ")
# arr = np.array([int(x) for x in user_input.split(',')])
# title = "Access 1-D Array | John Louie Ubias | 3 BSIT-2"
#
# print("Element at index 0:", arr[0])
# print("Sum of elements at index 2 and 3:", arr[2] + arr[3])
# print(title)

# Access 2-D Arrays
# import numpy as np
# rows = int(input("Enter the number of rows: "))
# cols = int(input("Enter the number of columns: "))
# arr = np.zeros((rows, cols), dtype=int)
#
# for i in range(rows):
#     user_input = input(f"Enter elements for row {i + 1} ({cols} elements, comma-separated): ")
#     arr[i] = [int(x) for x in user_input.split(',')]
# title = "Access 2-D Arrays | John Louie Ubias | 3 BSIT-2"
#
# print('2nd element on 1st row: ', arr[0, 1])
# print(title)


# Access 3-D Arrays
# import numpy as np
#
# depth = int(input("Enter the number of matrices: "))
# rows = int(input("Enter the number of rows in each matrix: "))
# cols = int(input("Enter the number of columns in each matrix: "))
# arr = np.zeros((depth, rows, cols), dtype=int)
#
# for d in range(depth):
#     print(f"Matrix {d + 1}:")
#     for i in range(rows):
#         user_input = input(f"  Enter elements for row {i + 1} (comma-separated): ")
#         arr[d, i] = [int(x) for x in user_input.split(',')]
# title = "Access 3-D Arrays | John Louie Ubias | 3 BSIT-2"
#
# print("Element at coordinates (0, 1, 2):", arr[0, 1, 2])
# print(title)


# Negative Indexing
# import numpy as np
#
# rows = int(input("Enter the number of rows: "))
# cols = int(input("Enter the number of columns: "))
# arr = np.zeros((rows, cols), dtype=int)
#
# for i in range(rows):
#     user_input = input(f"Enter elements for row {i + 1} (comma-separated): ")
#     arr[i] = [int(x) for x in user_input.split(',')]
# title = "Negative Indexing | John Louie Ubias | 3 BSIT-2"
#
# print('Last element from 2nd dim:', arr[1, -1])
# print(title)


# Slicing Arrays A
# import numpy as np
#
# user_input = input("Enter elements for the array (comma-separated): ")
# arr = np.array([int(x) for x in user_input.split(',')])
# title = "Slicing Arrays A | John Louie Ubias | 3 BSIT-2"
#
# start_index = int(input("Enter the start index for slicing: "))
# end_index = int(input("Enter the end index for slicing: "))
# print("Sliced array:", arr[start_index:end_index])
# print(title)


# Slicing Arrays B
# import numpy as np
#
# user_input = input("Enter elements for the array (comma-separated): ")
# arr = np.array([int(x) for x in user_input.split(',')])
#
# start_index = int(input("Enter the start index for slicing (inclusive): "))
# sliced_array = arr[start_index:]
# title = "Slicing Arrays B | John Louie Ubias | 3 BSIT-2"
#
# print("Sliced array:", sliced_array)
# print(title)


# Slicing Arrays C
# import numpy as np
#
# user_input = input("Enter elements for the array (comma-separated): ")
# arr = np.array([int(x) for x in user_input.split(',')])
#
# end_index = int(input("Enter the end index for slicing (exclusive): "))
# sliced_array = arr[:end_index]
# title = "Slicing Arrays C | John Louie Ubias | 3 BSIT-2"
#
# print("Sliced array:", sliced_array)
# print(title)


# Checking Data Types A
# import numpy as np
#
# user_input = input("Enter elements for the array (comma-separated): ")
# arr = np.array([int(x) for x in user_input.split(',')])
#
# title = "Checking Data Types A | John Louie Ubias | 3 BSIT-2"
# print(arr.dtype)
# print(title)


# Checking Data Types B
# import numpy as np
#
# user_input = input("Enter elements for the array (comma-separated): ")
# arr = np.array([x.strip() for x in user_input.split(',')])
#
# title = "Checking Data Types B | John Louie Ubias | 3 BSIT-2"
# print(arr.dtype)
# print(title)


# Creating Arrays With a Defined Data Type
# import numpy as np
#
# user_input = input("Enter elements for the array (comma-separated): ")
# data_type_input = input("Enter the desired data type (e.g., 'S' for string, 'i4' for int32): ")
# arr = np.array([x.strip() for x in user_input.split(',')], dtype=data_type_input)
# title = "Creating Arrays With a Defined Data Type | John Louie Ubias | 3 BSIT-2"
#
# print(arr)
# print(arr.dtype)
# print(title)


# Numpy Copy
# import numpy as np
#
# user_input = input("Enter elements for the array (comma-separated): ")
# arr = np.array([int(x) for x in user_input.split(',')])
# title = "Numpy Copy | John Louie Ubias | 3 BSIT-2"
# x = arr.copy()
# arr[0] = 42
#
# print(arr)
# print(x)
# print(title)

# Numpy View
# import numpy as np
#
# user_input = input("Enter elements for the array (comma-separated): ")
# arr = np.array([int(x) for x in user_input.split(',')])
#
# title = "Numpy View | John Louie Ubias | 3 BSIT-2"
# x = arr.view()
# arr[0] = 42
#
# print(arr)
# print(x)
# print(title)

# Get the Shape of an Array A
# import numpy as np
#
# rows = int(input("Enter the number of rows: "))
# cols = int(input("Enter the number of columns: "))
#
# arr = np.zeros((rows, cols), dtype=int)
#
# title = "Get the Shape of an Array A | John Louie Ubias | 3 BSIT-2"
# print(arr.shape)
# print(title)

# Get the Shape of an Array B
# import numpy as np
#
# user_input = input("Enter elements for the array (comma-separated): ")
# arr = np.array([int(x) for x in user_input.split(',')], ndmin=5)
#
# title = "Get the Shape of an Array B | John Louie Ubias | 3 BSIT-2"
# print(arr)
# print('shape of array:', arr.shape)
# print(title)


# Reshape From 1-D to 2-D
# import numpy as np
#
# user_input = input("Enter elements for the array (comma-separated): ")
# arr = np.array([int(x) for x in user_input.split(',')])
#
# title = "Reshape From 1-D to 2-D | John Louie Ubias | 3 BSIT-2"
# newarr = arr.reshape(4, 3)
#
# print(newarr)
# print(title)


# Reshape From 1-D to 3-D
# import numpy as np
#
# user_input = input("Enter elements for the array (comma-separated): ")
# arr = np.array([int(x) for x in user_input.split(',')])
#
# title = "Reshape From 1-D to 3-D | John Louie Ubias | 3 BSIT-2"
# newarr = arr.reshape(2, 3, 2)
#
# print(newarr)
# print(title)


# Iterating 1-D Array
# import numpy as np
#
# user_input = input("Enter elements for the array (comma-separated): ")
# arr = np.array([int(x) for x in user_input.split(',')])
#
# title = "Iterating 1-D Array | John Louie Ubias | 3 BSIT-2"
# for x in arr:
#     print(x)
# print(title)


# Iterating 2-D Arrays
# import numpy as np
#
# rows = int(input("Enter the number of rows: "))
# cols = int(input("Enter the number of columns: "))
#
# arr = np.zeros((rows, cols), dtype=int)
#
# title = "Iterating 2-D Arrays | John Louie Ubias | 3 BSIT-2"
# for x in arr:
#     print(x)
# print(title)


# Iterating 3-D Arrays
# import numpy as np
#
# depth = int(input("Enter the number of matrices: "))
# rows = int(input("Enter the number of rows in each matrix: "))
# cols = int(input("Enter the number of columns in each matrix: "))
#
# arr = np.zeros((depth, rows, cols), dtype=int)
#
# title = "Iterating 3-D Arrays | John Louie Ubias | 3 BSIT-2"
# for x in arr:
#     print(x)
# for x in arr:
#     for y in x:
#         for z in y:
#             print(z)
# print(title)

# Iterating Arrays Using nditer()
# import numpy as np
#
# depth = int(input("Enter the number of matrices: "))
# rows = int(input("Enter the number of rows in each matrix: "))
# cols = int(input("Enter the number of columns in each matrix: "))
#
# arr = np.zeros((depth, rows, cols), dtype=int)
#
# title = "Iterating Arrays Using nditer() | John Louie Ubias | 3 BSIT-2"
# for x in np.nditer(arr):
#     print(x)
# print(title)


# Iterating Array With Different Data Types
# import numpy as np
#
# user_input = input("Enter elements for the array (comma-separated): ")
# arr = np.array([int(x) for x in user_input.split(',')])
#
# title = "Iterating Array With Different Data Types | John Louie Ubias | 3 BSIT-2"
# for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
#     print(x)
# print(title)

