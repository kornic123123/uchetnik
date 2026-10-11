from flask import Flask, render_template


app = Flask(__name__)


@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('card.html')

@app.route('/student')
def student():
    return render_template('student.html')

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/task")
def task():
    return render_template(".html")





if __name__ == '__main__':
    app.run(debug=True)