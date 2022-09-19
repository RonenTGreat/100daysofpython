from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)

current_year = datetime.now().year



@app.route('/')
def home():
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number, year=current_year)


@app.route("/guess/<string:name>")
def guess(name):
    response_gender = requests.get(url=f"https://api.genderize.io/?name={name}")
    response_age = requests.get(url=f"https://api.agify.io/?name={name}")
    gender = response_gender.json()['gender']
    age = response_age.json()['age']

    return render_template("guess.html", name=name, gender=gender, age=age)


@app.route("/blog/<num>")
def blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", post=all_posts)


if __name__ == "__main__":
    app.run(debug=True)


