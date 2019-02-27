class Student:
    
    def __init__(self, first_name, last_name, gpa, major, advisor):
        self.first_name = first_name
        self.last_name = last_name
        self.gpa = gpa
        self.major = major
        self.advisor = advisor

    def get_student_info(self):
        student_tuple = (self.first_name, self.last_name, self.gpa, self.major, self.advisor)
        return student_tuple

