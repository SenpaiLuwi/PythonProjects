class Car:
    def __init__(self, color, model, manufacturer):
        self.color = color
        self.model = model
        self.manufacturer = manufacturer


# Create three Car objects
car1 = Car("", "", "")
car2 = Car("", "", "")
car3 = Car("", "", "")

# Input car properties from the user
car1.color = input("Enter Color for Car 1: ")
car1.model = input("Enter Model for Car 1: ")
car1.manufacturer = input("Enter Manufacturer for Car 1: ")

car2.color = input("\nEnter Color for Car 2: ")
car2.model = input("Enter Model for Car 2: ")
car2.manufacturer = input("Enter Manufacturer for Car 2: ")

car3.color = input("\nEnter Color for Car 3: ")
car3.model = input("Enter Model for Car 3: ")
car3.manufacturer = input("Enter Manufacturer for Car 3: ")

# Display the initial properties of the cars
print("\nInitial Properties of the Cars:")
print("Car 1 - Color:", car1.color)
print("Car 1 - Model:", car1.model)
print("Car 1 - Manufacturer:", car1.manufacturer)

print("\nCar 2 - Color:", car2.color)
print("Car 2 - Model:", car2.model)
print("Car 2 - Manufacturer:", car2.manufacturer)

print("\nCar 3 - Color:", car3.color)
print("Car 3 - Model:", car3.model)
print("Car 3 - Manufacturer:", car3.manufacturer)

# Modify car properties based on user input
print("\nModify Properties of the Cars:")
car1.color = input("Enter New Color for Car 1: ")
car1.model = input("Enter New Model for Car 1: ")
car1.manufacturer = input("Enter New Manufacturer for Car 1: ")
car2.color = input("\nEnter New Color for Car 2: ")
car2.model = input("Enter New Model for Car 2: ")
car2.manufacturer = input("Enter New Manufacturer for Car 2: ")
car3.color = input("\nEnter New Color for Car 3: ")
car3.model = input("Enter New Model for Car 3: ")
car3.manufacturer = input("Enter New Manufacturer for Car 3: ")

# Display the modified properties of the cars
print("\nModified Properties of the Cars:")
print("Car 1 - Color:", car1.color)
print("Car 1 - Model:", car1.model)
print("Car 1 - Manufacturer:", car1.manufacturer)

print("\nCar 2 - Color:", car2.color)
print("Car 2 - Model:", car2.model)
print("Car 2 - Manufacturer:", car2.manufacturer)

print("\nCar 3 - Color:", car3.color)
print("Car 3 - Model:", car3.model)
print("Car 3 - Manufacturer:", car3.manufacturer)
