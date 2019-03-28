
students = []

class Student:


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

student = Student("park")

print(student.get_name_capitalized())
print(student.__str__())

