from data import student

students = student()


class Student:
    _school_name = "Springfield Elementary"

    def __init__(self, name, last_name, student_id = 0):
        self.name = name
        self.last_name = last_name
        self.student_id = student_id
        student = {
        
            "name": self.name, 
            "last_name": self.last_name,
            "student_id": self.student_id
        
            }
        students.append(student)


    def __str__(self):
        return f"Student: {self.get_name_capitalized()}"
    

    def get_name_capitalized(self):
        return self.name.capitalize()


    def _get_school_name(self):
        return self._school_name