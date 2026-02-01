from student_manager import StudentManager

def menu():
    print("\n===== MENU =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Remove Student")
    print("5. Exit")

def main():
    print("Welcome to the Student Record Management System!")
    print("Loading student records from students.csv...")
    manager = StudentManager()
    print("Done!")

    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            manager.add_student()
        elif choice == "2":
            manager.view_students()
        elif choice == "3":
            manager.search_student()
        elif choice == "4":
            manager.remove_student()
        elif choice == "5":
            print("Thank you for using the Student Record Management System.")
            break
        else:
            print("Invalid choice. Please enter 1–5.")

if __name__ == "__main__":
    main()
