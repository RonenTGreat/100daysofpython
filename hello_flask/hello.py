from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return '<p style="color:blue;font-weight:bold;">Hello, World!</p>'

if __name__ == "__main__":
    app.run()
