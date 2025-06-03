# PY_OLA-1C_Ubias_NetSalary.py

import PYOLA1AUbiasSalary as salary
import PYOLA1BUbiasDeductions as deductions


def main():
    name, hours_worked, gross_salary = salary.compute_gross_salary()
    tax, loan, insurance, total_deductions = deductions.compute_deductions(gross_salary)
    net_salary = gross_salary - total_deductions

    print("\n\t\tEmployee")
    print("===============================")
    print(f"Name: \t\t\t\t{name}")
    print(f"Hour: \t\t\t\t{hours_worked}")
    print(f"Gross Salary: \t\t₱{gross_salary:.2f}")
    print("===============================")

    print("\n\t\tDeductions")
    print("===============================")
    print(f"Tax: \t\t\t\t₱{tax:.2f}")
    print(f"Loan: \t\t\t\t₱{loan:.2f}")
    print(f"Insurance: \t\t\t₱{insurance:.2f}")
    print(f"Total Deductions: \t₱{total_deductions:.2f}")
    print("===============================")

    print("\n\t\tNet Salary")
    print("===============================")
    print(f"Net Salary: \t\t₱{net_salary:.2f}")
    print("===============================")

    print("Programmed By John Louie Ubias | 3BSIT-2")


if __name__ == "__main__":
    main()
