students = []

def get_students_titlecase():
    students_titlecase = [student.title() for student in students]
    return students_titlecase

def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)

def add_student(name):
    students.append(name)