from flask import Flask, render_template
from data.base import Log
from forms.log_on import LoginForm
from flask_login import LoginManager, login_user
import os

SECRET_KEY = os.urandom(32)


app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/')
def ajr():
    return render_template('a.html')

@app.route('/log_on', methods=["POST", "GET"])
def loginig():
    form = LoginForm()
    return render_template("l_on.html", title="Авторизация", form=form)

if __name__ == '__main__':
    app.run(debug=True)

