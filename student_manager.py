import os
from student import Student

class StudentManager:
    def __init__(self, filename="students.csv"):
        self.filename = filename
        self.students = []
        self.load_students()

    def load_students(self):
        if not os.path.exists(self.filename):
            return

        with open(self.filename, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue  # skip empty lines

                data = line.split(",")
                if len(data) != 4:
                    continue  # skip invalid lines

                student = Student.from_csv(line)
                self.students.append(student)

    def save_students(self):
        with open(self.filename, "w") as file:
            for s in self.students:
                file.write(s.to_csv())

    def roll_exists(self, roll):
        for s in self.students:
            if s.roll == roll:
                return True
        return False

    def add_student(self):
        try:
            name = input("Enter Student Name: ").strip()
            if not name:
                print("Error: Name cannot be empty.")
                return

            roll = int(input("Enter Roll Number: "))
            if self.roll_exists(roll):
                print("Error: Roll number already exists for another student.")
                return

            email = input("Enter Email: ").strip()
            department = input("Enter Department: ").strip()

            if not email or not department:
                print("Error: Fields cannot be empty.")
                return

            student = Student(name, roll, email, department)
            self.students.append(student)
            self.save_students()
            print("Student record added successfully!")

        except ValueError:
            print("Error: Roll number must be an integer.")

    def view_students(self):
        if not self.students:
            print("No student records found.")
            return

        print("\n===== All Students =====")
        for i, s in enumerate(self.students, start=1):
            print(f"{i}. Name : {s.name}")
            print(f"   Roll : {s.roll}")
            print(f"   Email : {s.email}")
            print(f"   Department : {s.department}")
            print()

    def search_student(self):
        term = input("Enter search term (name/email/roll): ").lower()
        found = False

        for s in self.students:
            if (term in s.name.lower() or
                term in s.email.lower() or
                term == str(s.roll)):

                print("\nSearch Result:")
                print(f"Name : {s.name}")
                print(f"Roll : {s.roll}")
                print(f"Email : {s.email}")
                print(f"Department : {s.department}")
                found = True

        if not found:
            print("No matching student found.")

    def remove_student(self):
        try:
            roll = int(input("Enter the roll number of the student to delete: "))

            for s in self.students:
                if s.roll == roll:
                    confirm = input(f"Are you sure you want to delete student with roll number {roll}? (yes/no): ").lower()
                    if confirm == "yes":
                        self.students.remove(s)
                        self.save_students()
                        print("Student record deleted successfully!")
                    else:
                        print("Deletion cancelled.")
                    return

            print("Student not found.")

        except ValueError:
            print("Error: Roll number must be an integer.")
