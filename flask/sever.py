from typing import Dict

from flask import Flask, render_template, jsonify, request, redirect, url_for,flash

from app import index

app = Flask(__name__)

from database import session, StudentInfo
# from database import StudentInfo
from database import Tr


def myjsonify(data):
    response = jsonify(data)
    return response



# @app.route('/<name>')
# def home(name):
#     students = session.query(StudentInfo).filter(StudentInfo.name == name).first()
#     data = {
#         "title": "我的网站",
#         "user": {
#             "name": students.name,
#             "age": students.age,
#             "lesson": students.lesson,
#             "grade": students.grade,
#             "gender": students.gender
#         }, "Items": ["python", "jinjia2"]
#     }
#     return render_template('index.html', data=data)


@app.route("/login", methods=['GET', 'POST'])
def Login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        data = request.form
        username = data.get("username", None)
        password = data.get("password", None)
        tr = session.query(Tr).filter(Tr.username == username, Tr.password == password).first()
        if not tr:
            return render_template('login.html')
        else:
            return redirect(url_for("SeachStudents"))
@app.route("/search_for_students", methods=['GET', 'POST'])
def SeachStudents():
    if request.method == "POST":
        datas = request.form
        student_name = datas.get("student_name", None)
        print(student_name)
        students = session.query(StudentInfo).filter(StudentInfo.name == student_name).first()
        if students is None:
            data = {"user": {"name": "", "gender": 0,
                             "grade": "", "age": 0, "lesson": ""},
                    "Items": ["python", "jinjia2"]}
        else:
            data = {"user": {"name": students.name, "gender": students.gender,
                             "grade": students.grade, "age": students.age, "lesson": students.lesson},
                    "Items": ["python", "jinjia2"]}
    else:
        data = {"user": {"name": "", "gender": 0,
                         "grade": "", "age": 0, "lesson": ""},
                "Items": ["python", "jinjia2"]}
    return render_template('index.html', data=data)

@app.route("/sign_up", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'GET':
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]
        if password == confirm_password:
            students = session.query(StudentInfo).all()
            students_dict = {"username": username, "password": password,"id":len(students)}
            add_model = Tr(**students_dict)
            session.add(add_model)
            session.commit()
            print("sign up for True")
            return redirect(url_for("login"))
        else:
            return render_template("register.html")

if __name__ == '__main__':
    app.run(debug=True)
