# Check if a Function is an ufunc
import numpy as np

user_function_name = input("Enter a function name to check if it's a ufunc (e.g., add): ")

if type(getattr(np, user_function_name, None)) == np.ufunc:
    print(f'{user_function_name} is a ufunc')
else:
    print(f'{user_function_name} is not a ufunc')

title = "Check if a Function is a ufunc | John Louie Ubias | 3 BSIT-2"
print(title)