from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "Hello World"
@app.route("/greet/<name>")
def greet(name):
    return f"Hello,{name}!"
@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return f"{a} + {b} = {a + b}"
if __name__=="__main__":
    app.run(debug=True)

