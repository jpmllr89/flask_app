students = []

from classes import Student

#gets student name in students list and capitalizes it.
def get_students_titlecase():
    students_titlecase = []
    students_titlecase.append([student['name'].title() for student in students])
    return students_titlecase


#prints result from get_students_titlecase()
def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)



def add_student(name, student_id = 0):
    student = {
        
        "name":name, 
        "student_id": student_id
        
        }
    students.append(name)


#writes student variable to a txt file
def save_file(student):
    try:
        f = open("students.txt", "a")
        f.write(student + "\n")
        f.close()
    except Exception:
        print("Could not save file")

#a generator for reading lines in a file
def read_students(f):
    for line in f:
        yield line

#gets txt file and reads line and adds to student var
def read_file():
    try:
        f = open("students.txt", "r")
        for student in read_students(f):
            add_student(Student.students)
        f.close()
    
    except Exception:
        print("Could not read file")

