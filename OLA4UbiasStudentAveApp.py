class Student:
    def __init__(self, name, math_grade, science_grade, english_grade):
        self.name = name
        self.math_grade = math_grade
        self.science_grade = science_grade
        self.english_grade = english_grade

    def compute_average(self):
        return (self.math_grade + self.science_grade + self.english_grade) / 3

    def display_student_info(self):
        print(f"\nStudent Name: {self.name}")
        print(f"Math: {self.math_grade}")
        print(f"Science: {self.science_grade}")
        print(f"English: {self.english_grade}")
        average = self.compute_average()
        print(f"Average: {average} {'(Passed)' if average >= 60 else '(Failed)'}")


name = input("Enter Student's Name: ")
math_grade = float(input(f"Enter {name}'s Math Grade: "))
science_grade = float(input(f"Enter {name}'s Science Grade: "))
english_grade = float(input(f"Enter {name}'s English Grade: "))

student = Student(name, math_grade, science_grade, english_grade)

student.display_student_info()
