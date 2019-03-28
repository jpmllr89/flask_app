students = []

def get_students_titlecase():
    students_titlecase = [student['name'].title() for student in students]
    return students_titlecase

def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)

def add_student(name, student_id = 0):
    student = {
        
        "name":name, 
        "student_id": student_id
        
        }
    students.append(name)
