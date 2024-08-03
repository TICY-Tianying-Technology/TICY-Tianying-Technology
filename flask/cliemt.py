from flask import Flask, render_template, jsonify

app = Flask(__name__)
from database import session
# from database import StudentInfo


def myjsonify(data):
    response = jsonify(data)
    return response


@app.route('/student/', methods=['GET'])
def get_sutudent_info():
    # data_list = []
    students = session.query(StudentInfo.age).filter(StudentInfo.name == "韩七").first()
    data = {
        "age": students.age
    }
    return myjsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
