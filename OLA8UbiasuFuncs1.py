# Vectorization A
# user_input_x = input("Enter elements for the first list (comma-separated): ")
# user_input_y = input("Enter elements for the second list (comma-separated): ")
#
# x = [int(elem) for elem in user_input_x.split(',')]
# y = [int(elem) for elem in user_input_y.split(',')]
#
# z = [i + j for i, j in zip(x, y)]
#
# title = "Vectorization A | John Louie Ubias | 3 BSIT-2"
# print(z)
# print(title)


# Vectorization B
# import numpy as np
#
# user_input_x = input("Enter elements for the first list (comma-separated): ")
# user_input_y = input("Enter elements for the second list (comma-separated): ")
#
# x = np.array([int(elem) for elem in user_input_x.split(',')])
# y = np.array([int(elem) for elem in user_input_y.split(',')])
#
# z = np.add(x, y)
#
# title = "Vectorization B | John Louie Ubias | 3 BSIT-2"
# print(z)
# print(title)

# Addition Function
# import numpy as np
#
# user_input_x = input("Enter elements for the first list (comma-separated): ")
# user_input_y = input("Enter elements for the second list (comma-separated): ")
#
# x = np.array([int(elem) for elem in user_input_x.split(',')])
# y = np.array([int(elem) for elem in user_input_y.split(',')])
#
# myadd = np.frompyfunc(lambda a, b: a + b, 2, 1)
#
# title = "Addition Function | John Louie Ubias | 3 BSIT-2"
# print(myadd(x, y))
# print(title)


# Check if a Function is an ufunc
# import numpy as np
#
# user_function_name = input("Enter a function name to check if it's a ufunc (e.g., add): ")
#
# if type(getattr(np, user_function_name, None)) == np.ufunc:
#     print(f'{user_function_name} is a ufunc')
# else:
#     print(f'{user_function_name} is not a ufunc')
#
# title = "Check if a Function is a ufunc | John Louie Ubias | 3 BSIT-2"
# print(title)


# Addition
# import numpy as np
#
# user_input1 = input("Enter elements for the first array (comma-separated): ")
# user_input2 = input("Enter elements for the second array (comma-separated): ")
#
# arr1 = np.array([int(elem) for elem in user_input1.split(',')])
# arr2 = np.array([int(elem) for elem in user_input2.split(',')])
#
# newarr = np.add(arr1, arr2)
#
# title = "Addition | John Louie Ubias | 3 BSIT-2"
# print(newarr)
# print(title)

# Subtraction
# import numpy as np
#
# user_input1 = input("Enter elements for the first array (comma-separated): ")
# user_input2 = input("Enter elements for the second array (comma-separated): ")
#
# arr1 = np.array([int(elem) for elem in user_input1.split(',')])
# arr2 = np.array([int(elem) for elem in user_input2.split(',')])
#
# newarr = np.subtract(arr1, arr2)
#
# title = "Subtraction | John Louie Ubias | 3 BSIT-2"
# print(newarr)
# print(title)


# Multiplication
# import numpy as np
#
# user_input1 = input("Enter elements for the first array (comma-separated): ")
# user_input2 = input("Enter elements for the second array (comma-separated): ")
#
# arr1 = np.array([int(elem) for elem in user_input1.split(',')])
# arr2 = np.array([int(elem) for elem in user_input2.split(',')])
#
# newarr = np.multiply(arr1, arr2)
#
# title = "Multiplication | John Louie Ubias | 3 BSIT-2"
# print(newarr)
# print(title)

# Division
# import numpy as np
#
# user_input1 = input("Enter elements for the first array (comma-separated): ")
# user_input2 = input("Enter elements for the second array (comma-separated): ")
#
# arr1 = np.array([int(elem) for elem in user_input1.split(',')])
# arr2 = np.array([int(elem) for elem in user_input2.split(',')])
#
# newarr = np.divide(arr1, arr2)
#
# title = "Division | John Louie Ubias | 3 BSIT-2"
# print(newarr)
# print(title)


# Log at Base 2
# import numpy as np
#
# user_input = input("Enter elements for the array (comma-separated): ")
#
# arr = np.array([int(elem) for elem in user_input.split(',')])
#
# title = "Log at Base 2 | John Louie Ubias | 3 BSIT-2"
# print(np.log2(arr))
# print(title)


# NumPy Summations
# import numpy as np
#
# user_input1 = input("Enter elements for the first array (comma-separated): ")
# user_input2 = input("Enter elements for the second array (comma-separated): ")
#
# arr1 = np.array([int(elem) for elem in user_input1.split(',')])
# arr2 = np.array([int(elem) for elem in user_input2.split(',')])
#
# newarr = np.add(arr1, arr2)
#
# title = "NumPy Summations | John Louie Ubias | 3 BSIT-2"
# print(newarr)
# print(title)

# Summation Over an Axis
# import numpy as np
#
# user_input1 = input("Enter elements for the first array (comma-separated): ")
# user_input2 = input("Enter elements for the second array (comma-separated): ")
#
# arr1 = np.array([int(elem) for elem in user_input1.split(',')])
# arr2 = np.array([int(elem) for elem in user_input2.split(',')])
#
# newarr = np.sum([arr1, arr2], axis=1)
#
# title = "NumPy Summations | John Louie Ubias | 3 BSIT-2"
# print(newarr)
# print(title)


# Cummulative Sum
# import numpy as np
#
# user_input = input("Enter elements for the array (comma-separated): ")
# array = np.array([int(elem) for elem in user_input.split(',')])
#
# cumulative_sum_result = np.cumsum(array)
#
# title = "Cumulative Sum | John Louie Ubias | 3 BSIT-2"
# print(cumulative_sum_result)
# print(title)

