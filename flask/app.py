from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/index/<number>", methods=["GET"])
def index(number):
    return f"number {number}"
{"username": "张三",
 "password": "1234567"}


@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", "")
    password = request.json.get("password", "")
    print("username", username)
    print("password", password)

    return 111

if __name__ == "__main__":
    app.run()