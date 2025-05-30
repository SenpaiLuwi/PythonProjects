def calculate_average(name, math_grade, english_grade, science_grade):
    average = (math_grade + english_grade + science_grade) / 3
    print(name)
    print("Math = {}, English = {}, Science = {}".format(math_grade, english_grade, science_grade))
    print(f"Average = {average:.2f}")
    print()


# Get user input for each student's grades
eunice_math = float(input("Eunice's math grade: "))
eunice_english = float(input("Eunice's english grade: "))
eunice_science = float(input("Eunice's science grade: "))
print("")

james_math = float(input("James's math grade: "))
james_english = float(input("James's english grade: "))
james_science = float(input("James's science grade: "))
print("")

john_math = float(input("John's math grade: "))
john_english = float(input("John's english grade: "))
john_science = float(input("John's science grade: "))

# Call the calculate_average function for each student
calculate_average("\nEunice", eunice_math, eunice_english, eunice_science)
calculate_average("James", james_math, james_english, james_science)
calculate_average("John", john_math, john_english, john_science)
