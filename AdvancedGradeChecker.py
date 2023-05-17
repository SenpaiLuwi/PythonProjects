def calculate_average(name, grades):
    total_grades = sum(grades)
    average = total_grades / len(grades)
    print(name)
    print("Grades: {}".format(", ".join(map(str, grades))))
    print("Average = {:.2f}".format(average))
    print()


def get_valid_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer.")
                continue
            return value
        except ValueError:
            print("Please enter a valid integer.")


def get_valid_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid floating-point number.")


def input_grades(subjects):
    grades = []
    for subject in subjects:
        grade = get_valid_float_input("{} grade: ".format(subject))
        grades.append(grade)
    print()
    return grades


# Get the number of students
num_students = get_valid_integer_input("Enter the number of students: ")

students = []
for i in range(num_students):
    print("\nStudent #{}".format(i + 1))

    # Get the student's name
    name = input("Enter the student's name: ")

    # Get the number of subjects
    num_subjects = get_valid_integer_input("Enter the number of subjects: ")

    subjects = []
    for j in range(num_subjects):
        subject = input("Enter subject #{}: ".format(j + 1))
        subjects.append(subject)

    print()

    # Input grades for the student
    grades = input_grades(subjects)

    # Create a dictionary for the student
    student = {
        "name": name,
        "grades": grades
    }

    students.append(student)

# Calculate and display average for each student
for student in students:
    calculate_average(student["name"], student["grades"])
