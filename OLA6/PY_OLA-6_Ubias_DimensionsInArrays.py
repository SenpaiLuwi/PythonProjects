import numpy as np
input_a = input("Enter a single element for array 'a': ")
a = np.array(int(input_a))
input_b = input("Enter elements for array 'b' (comma-separated): ")
b = np.array([int(x) for x in input_b.split(',')])
input_c = input("Enter elements for a 2D array 'c' (comma-separated, rows separated by semicolon): ")
c = np.array([list(map(int, row.split(','))) for row in input_c.split(';')])
input_d = input("Enter elements for a 3D array 'd' (semicolon-separated, matrices separated by pipe): ")
d = np.array([[[int(z) for z in item.split(',')] for item in row.split(';')] for row in input_d.split('|')])
title = "Dimensions in Arrays | John Louie Ubias | 3 BSIT-2"

print("Dimension of array 'a':", a.ndim)
print("Dimension of array 'b':", b.ndim)
print("Dimension of array 'c':", c.ndim)
print("Dimension of array 'd':", d.ndim)
print(title)
