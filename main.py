from student import Student
import data
from hs_student import *
import functions as f
from flask import Flask, render_template, redirect, url_for, request, flash, session, logging
from flask_mysqldb import MySQL
from register_form import RegisterForm
from passlib.hash import sha256_crypt


students = data.student()

app = Flask(__name__)

#config mySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'jpmllr89'
app.config['MYSQL_PASSWORD'] = 'ninetails.666'
app.config['MYSQL_DB'] = 'StudentFlaskApp'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

#initialize mySQL
mysql = MySQL(app)


# Home Page
@app.route("/", methods = ['GET', 'POST'])
def about():
    return render_template("about.html")

#List of Students Page
@app.route("/students_list", methods = ['GET', 'POST'])
def students_list():
    return render_template("students.html", students = students)

#Delete/edit page

@app.route("/students_list/", methods = ['GET', 'POST', 'UPDATE'])
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


@app.route('/register', methods = ['GET', 'POST']) 
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
            user_name = form.user_name.data 
            email = form.email.data
            password = sha256_crypt.encrypt(str(form.password.data))
            
            #creating the cursor to execute demands
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO users(user_name, email, password) VALUES(%s, %s, %s, %s)", (user_name, email, password))
            msql.connection.commit()

            cur.close()

            flash("You are now registered and can login", 'success')

            redirect(url_for('index'))

        
    return render_template('register.html', form = form) 


#Start app if program name is main
if __name__ == "__main__":
    app.run()