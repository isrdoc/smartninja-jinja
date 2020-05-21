from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    title = "Mainpage"
    time_now = datetime.now()
    people = ["Janko", "Metka", "Jure"]

    return render_template("index.html", title=title, time_now=time_now, people=people)


@app.route('/about')
def about():
    title = "About Jinja"
    return render_template("about.html", title=title)


if __name__ == '__main__':
    app.run()
