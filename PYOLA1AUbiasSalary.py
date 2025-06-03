# PY_OLA-1A_Ubias_Salary.py

def compute_gross_salary():
    name = input("Enter your name: ")
    while True:
        try:
            hours_worked = float(input("Enter Hours worked: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for hours worked.")
    rate_per_hour = 500.00
    gross_salary = hours_worked * rate_per_hour
    print("===Summary===")
    print("Name:", name)
    print("Hours Worked", hours_worked)
    print("Gross Salary", gross_salary)
    print()
    return name, hours_worked, gross_salary
