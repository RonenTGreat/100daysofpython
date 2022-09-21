from flask import Flask, render_template
from post import Post

app = Flask(__name__)

post = Post()
all_blogs = post.all_blogs

print(all_blogs)

@app.route('/')
def home():
    return render_template("index.html", all_blogs=all_blogs)

@app.route('/post/<int:num>')
def blogs(num):
    return render_template("post.html", all_blogs=all_blogs, num=num)


if __name__ == "__main__":
    app.run(debug=True)
