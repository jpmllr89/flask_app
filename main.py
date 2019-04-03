from student import Student
from hs_student import *
import functions as f
from flask import Flask, render_template, redirect, url_for, request, flash, session, logging
from flask_mysqldb import mysql 
from wtforms import form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt


students = []

app = Flask(__name__)


# Home Page
@app.route("/", methods = ['GET', 'POST'])
def about():
    return render_template("about.html")

#List of Students Page
@app.route("/students_list", methods = ['GET', 'POST'])
def students_list():
    return render_template("students.html", students = students)

#Delete/edit page

@app.route("/students_list/<string: id>/", methods = ['GET', 'POST', 'UPDATE'])
def edit_student(id):
    return render_template("students.html", id = student.student_id)

#Add a Student Page
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


#with wt forms you have to create a class for the form you are creating.
class RegisterForm(Form):
    user_name = StringField('User Name', [validators.Length(min = 4, max = 25)])
    email = StringField('Email: ', [validators.Length(min = 6, max = 25)])
    password = StringField('Password: ', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message="Passwords do not match")
        ]
    )
    confirm = PasswordField('Confirm Password')

@app.route('/register', methods = ['GET', 'POST']) 
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():

    return render_template('register.html', form = form) 
#Start app if program name is main
if __name__ == "__main__":
    app.run()