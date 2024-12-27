from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>welcome to the home page!<h1>"

@app.route("/welcome/<name>")
def welcome(name):
    return f"<h1>Hi {name}, you are welcome to this page!<h1>"


@app.route("/about")
def about():
    return "<h1>welcome to the about page!<h1>"

@app.route("/addition/<int:num1>/<int:num2>")
def addition(num1, num2):
    return f"<h1>input is {num1} and {num2} and  output is {num1 + num2}<h1>"


if __name__ == "__main__":
    app.run(debug=True)


