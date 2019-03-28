
students = []

class Student:
    def __init__(self, name, student_id = 0):
        student = {
        
            "name":name, 
            "student_id": student_id
        
            }
        students.append(student)

    def __str__(self):
        return f"Student: {self.name}"

student = Student()

