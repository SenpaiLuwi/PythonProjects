import numpy as np

def main():
    print("OLA10 | ROUNDDEC | UBIAS, JOHN LOUIE | 3 BSIT-2")
    print("Rounding Decimals and Summation")
    print("[1] Truncation")
    print("[2] Rounding")
    print("[3] Floor")
    print("[4] Ceiling")
    print("[5] Summation")
    print("[6] Cumulative Summation")

    choice = get_valid_input("Please enter your choice: ")

    size = int(get_valid_input("\nEnter size of the array: "))
    arrayInput = np.zeros(size)

    print(f"Enter elements for array ({size} elements):")
    for i in range(size):
        arrayInput[i] = get_valid_input(f"Enter element {i + 1}: ")

    if choice == 1:
        result = np.trunc(arrayInput)
        print(f"Output is {result}.")
        print("Truncation | UBIAS, JOHN LOUIE | 3 BSIT-2")
    elif choice == 2:
        result = np.round(arrayInput)
        print(f"Output is {result}.")
        print("Rounding | UBIAS, JOHN LOUIE | 3 BSIT-2")
    elif choice == 3:
        result = np.floor(arrayInput)
        print(f"Output is {result}.")
        print("Floor | UBIAS, JOHN LOUIE | 3 BSIT-2")
    elif choice == 4:
        result = np.ceil(arrayInput)
        print(f"Output is {result}.")
        print("Ceiling | UBIAS, JOHN LOUIE | 3 BSIT-2")
    elif choice == 5:
        result = np.sum(arrayInput)
        print(f"Summation is {result}.")
        print("Summation | UBIAS, JOHN LOUIE | 3 BSIT-2")
    elif choice == 6:
        result = np.cumsum(arrayInput)
        print(f"Cumulative Summation is {result}.")
        print("Cumulative | UBIAS, JOHN LOUIE | 3 BSIT-2")
    else:
        print("Invalid choice. Please choose a number between 1 and 6.")

def get_valid_input(message):
    while True:
        try:
            value = float(input(message))
            return value
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
