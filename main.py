import pandas as pd

class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def get_average_grade(self):
        return sum(self.grades.values()) / len(self.grades)

class StudentPerformanceTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name, roll_number):
        self.students[roll_number] = Student(name, roll_number)

    def add_grade(self, roll_number, subject, grade):
        if roll_number in self.students:
            self.students[roll_number].add_grade(subject, grade)
        else:
            print("Student not found.")

    def get_student_average(self, roll_number):
        if roll_number in self.students:
            return self.students[roll_number].get_average_grade()
        else:
            print("Student not found.")

    def get_student_report(self, roll_number):
        if roll_number in self.students:
            student = self.students[roll_number]
            print(f"Name: {student.name}")
            print(f"Roll Number: {student.roll_number}")
            print("Grades:")
            for subject, grade in student.grades.items():
                print(f"{subject}: {grade}")
            print(f"Average Grade: {student.get_average_grade()}")
        else:
            print("Student not found.")

def main():
    tracker = StudentPerformanceTracker()

    while True:
        print("\nStudent Performance Tracker")
        print("1. Add Student")
        print("2. Add Grade")
        print("3. Get Student Average")
        print("4. Get Student Report")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter student name: ")
            roll_number = input("Enter roll number: ")
            tracker.add_student(name, roll_number)
        elif choice == "2":
            roll_number = input("Enter roll number: ")
            subject = input("Enter subject: ")
            grade = float(input("Enter grade: "))
            tracker.add_grade(roll_number, subject, grade)
        elif choice == "3":
            roll_number = input("Enter roll number: ")
            print(tracker.get_student_average(roll_number))
        elif choice == "4":
            roll_number = input("Enter roll number: ")
            tracker.get_student_report(roll_number)
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()