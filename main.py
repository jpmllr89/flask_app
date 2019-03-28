from student import Student
from hs_student import *
import functions as f
from flask import Flask, render_template, redirect, url_for, request

students = []

app = Flask(__name__)



@app.route("/", methods = ['GET', 'POST'])
def about():
    return render_template("about.html")


@app.route("/students_list", methods = ['GET', 'POST'])
def students_list():
    return render_template("students.html", students = students)


@app.route("/add_student", methods = ['GET', 'POST'])
def add_student():
    if request.method =="POST":
        new_student_id = request.form.get("student-id", "")
        new_student_name = request.form.get("name", "")
        new_student_last_name = request.form.get("last-name", "")

        new_student = Student(name=new_student_name, last_name = new_student_last_name, student_id=new_student_id)
        students.append(new_student)

        return redirect(url_for("students_page"))
    return render_template("add.html", students=students)


if __name__ == "__main__":
    app.run(debug = True)