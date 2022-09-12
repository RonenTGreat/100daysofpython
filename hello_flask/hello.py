from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return '<p style="color:red;font-weight:bold;">Hello, World!</p>'