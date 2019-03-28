
students = []

class Student:

    _school_name = "Springfield Elementary"

    def __init__(self, name, student_id = 0):
        self.name = name
        self.student_id = student_id
        student = {
        
            "name": self.name, 
            "student_id": self.student_id
        
            }
        students.append(student)


    def __str__(self):
        return f"Student: {self.get_name_capitalized()}"
    

    def get_name_capitalized(self):
        return self.name.capitalize()


    def _get_school_name(self):
        return self._school_name


class HighSchoolStudent(Student):

    _school_name = "Springfield High"

    def _get_school_name(self):
        return f"{self.get_name_capitalized()} from {super()._get_school_name()}"
