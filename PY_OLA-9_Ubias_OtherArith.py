import numpy as np

def main():
    print("OLA9 | OTHER ARITH | UBIAS, JOHN LOUIE | 3 BSIT-2")
    print("Simple Arithmetic Operations")
    print("[1] Power")
    print("[2] Remainder")
    print("[3] Quotient")
    print("[4] Absolute")

    choice = get_valid_input("Please enter your choice (Number Only): ")

    size = int(get_valid_input("\nEnter size of the array(Number Only): "))
    arrayInput = np.zeros(size)

    print(f"Enter elements for array 1 ({size} elements):")
    for i in range(size):
        arrayInput[i] = get_valid_input(f"Enter element {i + 1}: ")

    if choice == 1:
        exponent = get_valid_input("Enter the exponent for power calculation: ")
        result = np.power(arrayInput, exponent)
        print(f"\nPower value is {result},")
        print("Power | UBIAS, JOHN LOUIE | 3 BSIT-2")
    elif choice == 2:
        divisor = get_valid_input("Enter the divisor for remainder calculation: ")
        result = np.remainder(arrayInput, divisor)
        print(f"\nRemainder values are {result},")
        print("Remainder | UBIAS, JOHN LOUIE | 3 BSIT-2")
    elif choice == 3:
        divisor = get_valid_input("Enter the divisor for quotient and remainder calculation: ")
        quotient, remainder = np.divmod(arrayInput, divisor)
        print(f"\nQuotient values are {quotient},")
        print(f"Remainder values are {remainder}.")
        print("Quotient | UBIAS, JOHN LOUIE | 3 BSIT-2")
    elif choice == 4:
        result = np.absolute(arrayInput)
        print(f"\nAbsolute values are {result},")
        print("Absolute | UBIAS, JOHN LOUIE | 3 BSIT-2")
    else:
        print("Invalid choice. Please choose a number between 1 and 4.")

def get_valid_input(message):
    while True:
        try:
            value = float(input(message))
            return value
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
