from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9</h1>"


if __name__ == "__main__":
    app.run(debug=True)