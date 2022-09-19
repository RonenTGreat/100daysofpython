from flask import Flask, render_template
import random
from datetime import datetime

app = Flask(__name__)

current_year = datetime.now().year



@app.route('/')
def home():
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number, year=current_year)


@app.route("/guess/<string:name>")
def guess(name):
    return f"{name}"


if __name__ == "__main__":
    app.run(debug=True)


