from flask import Flask, render_template, request
from data.base import Log
from photo import found
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
   if request.method == 'POST':
        a, image = request.form['all'], request.form['image']
        if a != '':
            f = found(image, a)
            if f != []:
                return render_template("l_on.html", result=f)
        Log(log=request.form['login'], em=request.form['email'],
            pas=request.form['psw1'], al=a)
        return render_template("l_on.html", title="Авторизация")
   else:
        return render_template('l_on.html')


if __name__ == '__main__':
    app.run(debug=True)
