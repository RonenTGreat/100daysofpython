from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return '<p style="color:blue;font-weight:bold;">Hello, World!</p>'


@app.route("/resume")
def resume():
    return (
        "<div>"
        
        '<h1 style="text-align:center;">Ronen Nii Ayi Hammond</h2>'
        '<h4 style="text-align:center;">Accra-Ghana, Phone: +233543677965</h4>'
        '<h4 style="text-align:center;">ronenhammond@gmail.com</h4>'
        "<h2>Education</h2>"
        "<hr />"
        '<h3>University of Ghana</h3>'
        '<p>Programme: Bachelor of Science, Information Technology <span style="text-align:right; margin-left: 30rem">'
        'Expected September 2024</span></p>'
        '<p>Academic Standing: Second Upper</p>'
        '<p>Relevant Courses: Introduction to Computer Science, Programming Fundamentals, Programming I, Introduction t'
        'oEconomics, Mathematics for IT Professionals, Date Structures and Algorithms, Office Productivity Tools, '
        'Software Engineering, Multimedia and Web Development</p>'
        "</div>"
    )


@app.route("/<name>")
def greet(name):
    return f"Hello {name}"


def make_bold(function):
    def wrapper_function():
        return f"<b>{function()}</b>"
    return wrapper_function


def make_emphasis(function):
    def wrapper_function():
        return f"<em>{function()}</em>"
    return wrapper_function


def make_underlined(function):
    def wrapper_function():
        return f"<u>{function()}</u>"
    return wrapper_function


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye"


if __name__ == "__main__":
    app.run(debug=True)
