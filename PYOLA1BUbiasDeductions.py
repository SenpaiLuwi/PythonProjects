# PY_OLA-1B_Ubias_Deductions.py

def compute_deductions(gross_salary):
    tax = 0.12 * gross_salary

    while True:
        try:
            loan = float(input("Enter Loan: ₱ "))
            break
        except ValueError:
            print("Invalid input for Loan. Please enter a valid amount.")
    while True:
        try:
            insurance = float(input("Enter Insurance: ₱ "))
            break
        except ValueError:
            print("Invalid input for Insurance. Please enter a valid amount.")
    total_deductions = tax + loan + insurance
    print("===Summary===")
    print("Tax:", tax)
    print("Loan", loan)
    print("Total Deductions", total_deductions)
    print()
    return tax, loan, insurance, total_deductions
