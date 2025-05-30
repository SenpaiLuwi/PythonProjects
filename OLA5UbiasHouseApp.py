class House:
    def __init__(self, floorSize, noOfFloors, noOfDoors):
        self.floorSize = floorSize
        self.noOfFloors = noOfFloors
        self.noOfDoors = noOfDoors

    @staticmethod
    def lightOpen():
        print("The Lights will be turned ON")

    @staticmethod
    def ovenOpen():
        print("The Oven will be turned ON")


class TownHouse(House):
    def __init__(self, floorSize, noOfFloors, noOfDoors, noOfWindows):
        super().__init__(floorSize, noOfFloors, noOfDoors)
        self.noOfWindows = noOfWindows

    def switchOn(self):
        self.lightOpen()
        self.ovenOpen()


floorSize = float(input("Enter floor size (sq ft): "))
noOfFloors = int(input("Enter number of floors: "))
noOfDoors = int(input("Enter number of doors: "))
noOfWindows = int(input("Enter number of windows: "))

townhouse = TownHouse(floorSize, noOfFloors, noOfDoors, noOfWindows)

print("\nTownHouse Properties:")
print("Floor Size:", townhouse.floorSize, "sq ft")
print("Number of Floors:", townhouse.noOfFloors)
print("Number of Doors:", townhouse.noOfDoors)
print("Number of Windows:", townhouse.noOfWindows)

print("\nTurning On TownHouse:")
townhouse.switchOn()
