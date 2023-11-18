from flask import Flask, render_template, request
from data.base import Log
from forms.register import LoginForm
from flask_login import LoginManager, login_user
import os

SECRET_KEY = os.urandom(32)


app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/')
def ajr():
    return render_template('a.html')

@app.route('/registration', methods=["POST", "GET"])
def register():
    form = LoginForm()
    if request.method == 'POST':

        try:
            Log(request.form['login'], request.form['email'],
                request.form['psw1'], request.form['all'])
        except:
            Log(error=1)
    return render_template("l_on.html", title="Авторизация", form=form, error=0)

if __name__ == '__main__':
    app.run(debug=True)

