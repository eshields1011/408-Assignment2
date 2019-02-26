import sqlite3
# From Student import Student

conn = sqlite3.connect("StudentDB.db")
c = conn.cursor()

while True:
        print("""Press (a) to display all students 
Press (b) to create a new student 
Press (c) to update an existing student
Press (d) to delete a student
Press (e) to query students
Press (q) to quit""")
        command = raw_input("Enter your decision: ")

        if command == "a":
                for row in c.execute('SELECT * FROM StudentDB'):
                        print row

        elif command == "b":
                first_name = raw_input("Enter the student's first name: ")
                last_name = raw_input("Enter the student's last name: ")
                major = raw_input("Enter the student's major: ")
                advisor = raw_input("Enter the student's faculty advisor: ")
                gpa = raw_input("Enter the student's GPA: ")

                while True:
                        try:
                                gpa = float(gpa)
                                break

                        except ValueError:
                                print("User input was not a valid number. Please try again")
                                gpa = raw_input("Enter the student's GPA: ")

                data = (first_name, last_name, gpa, major, advisor)
                c.execute('INSERT INTO StudentDB(FirstName, LastName, GPA, Major, FacultyAdvisor) VALUES (?,?,?,?,?)', data)
                del data
                print("Successfully added student")

        elif command == "c":
                student_id = raw_input("Enter the id of the student to be updated: ")
                while True:
                        try:
                                student_id = int(student_id)
                                break

                        except ValueError:
                                print("User input was not a valid number. Please try again")
                                student_id = raw_input("Enter the specific student's id: ")

                new_major = raw_input("Enter the student's updated major: ")
                new_advisor = raw_input("Enter the student's updated faculty advisor: ")
                update_tuple = (new_major, new_advisor, student_id)
                c.execute('UPDATE StudentDB SET Major = ?, FacultyAdvisor = ? WHERE StudentId = ?', update_tuple)
                del update_tuple

        elif command == "d":
                student_id = raw_input("Enter the specific student's id: ")
                while True:
                        try:
                                student_id = int(student_id)
                                break

                        except ValueError:
                                print("User input was not a valid number. Please try again")
                                student_id = raw_input("Enter the specific student's id: ")
                tuple_id = (student_id,)
                c.execute('DELETE FROM StudentDB WHERE StudentId = ?', tuple_id)
                del tuple_id

        elif command == "e":
                while True:
                        search = raw_input("Press (m) to query by major, (g) for gpa, or (a) for advisor: ")
                        if search == "m":
                                major_query = raw_input("Enter the major you are searching for: ")
                                major_tuple = (major_query,)
                                print("Students majoring in " + major_query + ": ")
                                for row in c.execute('SELECT * FROM StudentDB WHERE Major = ?', major_tuple):
                                        print row
                                del major_tuple
                                break

                        elif search == "g":
                                gpa_query = raw_input("Enter the GPA you are searching for: ")
                                while True:
                                        try:
                                                gpa_query = float(gpa_query)
                                                break

                                        except ValueError:
                                                print("User input was not a valid number. Please try again")
                                                gpa_query = raw_input("Enter the GPA you are searching for: ")

                                gpa_tuple = (gpa_query,)
                                print("Students with a GPA of " + str(gpa_query) + ": ")
                                for row in c.execute('SELECT * FROM StudentDB WHERE GPA = ?', gpa_tuple):
                                        print row
                                del gpa_tuple
                                break

                        elif search == "a":
                                advisor_query = raw_input("Enter the advisor you are looking for: ")
                                advisor_tuple = (advisor_query,)
                                print("Students whose advisor is " + advisor_query + ": ")
                                for row in c.execute('SELECT * FROM StudentDB WHERE FacultyAdvisor = ?', advisor_tuple):
                                        print row
                                del advisor_tuple
                                break

                        else:
                                print("Invalid input. Please try again")

        elif command == "q":
                print("Exiting program...")
                break
        else:
                print("Invalid input. Please try again")

        print("")

