import sqlite3
import Student
import Methods

methods = Methods.Methods()
while True:
        print("""Press (a) to display all students 
Press (b) to create a new student 
Press (c) to update an existing student
Press (d) to delete a student
Press (e) to query students
Press (q) to quit""")
        command = raw_input("Enter your decision: ")

        if command == "a":
                methods.print_all()

        elif command == "b":
                methods.create_student()

        elif command == "c":
                methods.update_student()

        elif command == "d":
                methods.delete_student()

        elif command == "e":
                methods.query()

        elif command == "q":
                print("Exiting program...")
                break
        else:
                print("Invalid input. Please try again")

        print("")
