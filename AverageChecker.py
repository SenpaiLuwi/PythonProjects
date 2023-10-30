def main() -> object:
    # get the number of students
    num_students = int(input("Enter the number of students: "))

    # get the number of subjects
    num_subjects = int(input("Enter the number of subjects: "))

    # create an empty list to store student names and grades
    student_grades = []

    # get the grades for each student and subject
    for i in range(num_students):
        student_name = input("Enter the student's name (Last Name, First Name, Middle Initial): ")
        grades = {}

        for j in range(num_subjects):
            subject_name = input("Enter the subject name: ")
            grade = float(input(f"Enter {student_name}'s grade in {subject_name}: "))
            grades[subject_name] = grade

        student_grades.append((student_name, grades))

    # calculate the average grade for each student
    for student, grades in student_grades:
        average_grade = sum(grades.values()) / num_subjects
        print(f"The average grade for {student} is: {'%.2f' % average_grade}")


if __name__ == '__main__':
    main()


# https://github.com/SenpaiLuwi
