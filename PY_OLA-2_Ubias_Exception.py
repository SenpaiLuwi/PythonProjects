#PY_OLA-2_Ubias_Exception.py

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        raise ValueError()
    return x / y


while True:
    print()
    print("===============================")
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Quit (:<)")
    print("===============================")

    try:
        number = int(input("Enter choice (1/2/3/4/5): "))
        if number == 5:
            break
        if number not in [1, 2, 3, 4]:
            print("Invalid choice. Please select a valid operation (1/2/3/4/5).")
            continue

        print()
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if number == 1:
            result = add(num1, num2)
        elif number == 2:
            result = subtract(num1, num2)
        elif number == 3:
            result = multiply(num1, num2)
        elif number == 4:
            try:
                result = divide(num1, num2)
            except ValueError:
                print("Division by zero is not allowed.")
                continue
        print("Result:", result)

        while True:
            print()
            print("===============================")
            retry = input("Do you want to try again? (yes/no/y/n): ").lower()
            if retry in ["yes", "no", "y", "n"]:
                break
            else:
                print("Invalid input. Please enter 'yes', 'no', 'y', 'n'")
        if retry == "no":
            break

    except ValueError:
        print("Invalid input. The Input must NOT be Empty or String")

print("Thank you for Using Calculator. Programmed By John Louie Ubias | 3BSIT-2")
