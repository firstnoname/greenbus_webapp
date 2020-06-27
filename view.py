from flask import Flask, render_template
from Timetable import *
from User import *
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "greenbus"
app.permanent_session_lifetime = timedelta(minutes=15)
app.register_blueprint(timetable)
app.register_blueprint(user)

@app.route("/")
def index():
    return render_template('User/login.html', header_name = "Hello GB")


if __name__ == '__main__':
    app.run(debug = True)
