def main() -> object:
    # get the student's name
    name = input("Enter the student's name (Last Name, Fist Name, Middle Initial): ")

    # get the student's grades
    math_grade = float(input("Enter the student's grade in Math: "))
    science_grade = float(input("Enter the student's grade in Science: "))
    english_grade = float(input("Enter the student's grade in English: "))

    # calculate the average grade
    average_grade = (math_grade + science_grade + english_grade) / 3

    # print the result
    print("The average grade for", name, "is:", "%.2f" % average_grade)


if __name__ == '__main__':
    main()
