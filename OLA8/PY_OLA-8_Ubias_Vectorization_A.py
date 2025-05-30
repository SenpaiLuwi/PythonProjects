# Vectorization A
user_input_x = input("Enter elements for the first list (comma-separated): ")
user_input_y = input("Enter elements for the second list (comma-separated): ")

x = [int(elem) for elem in user_input_x.split(',')]
y = [int(elem) for elem in user_input_y.split(',')]

z = [i + j for i, j in zip(x, y)]

title = "Vectorization A | John Louie Ubias | 3 BSIT-2"
print(z)
print(title)