# define a function to calculate the bonus
def calculate_bonus(years, office):
    if office == 'IT':
        if years > 10:
            return 10000
        else:
            return 5000
    elif office == 'ACCT':
        if years > 10:
            return 12000
        else:
            return 6000
    elif office == 'HR':
        if years > 10:
            return 15000
        else:
            return 7500
    else:
        return 0


print("Developed by: Ubias, John Louie M. | 2 BSIT-2 \n")

# ask the user to input the number of employees to calculate the bonus for
num_employees = int(input("How many employees do you want to calculate the bonus for? "))

for i in range(num_employees):

    # ask the user to input the employee's name
    name = input(f"\nEnter the employee's name ({i + 1}/{num_employees}): ")

    # ask the user to input the number of years the employee has been in service
    years = int(input(f"Enter the number of years {name} has been in service: "))

    # ask the user to input the employee's office
    office = input(f"Enter {name}'s department (IT, ACCT, HR): ")

    # calculate the bonus using the calculate_bonus function
    bonus = calculate_bonus(years, office)

    # print the result
    print(f"Hi {name}, your bonus is {bonus}")
   

