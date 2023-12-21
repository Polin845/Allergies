from flask import Flask, render_template, request, redirect, url_for
from data import dase
from data.users import User
from photo import found
from flask_login import LoginManager, login_user
import os

SECRET_KEY = os.urandom(32)
dase.global_init("db/blogs.db")


app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

user = User()


@app.route('/', methods=["POST", "GET"])
def lobby():
   if request.method == 'POST':
        a = request.form['all']
        image = request.files['file']
        if a != '':
            f = found(image, a)
            if f != []:
                return render_template("lobby.html", result=f)
        return render_template("lobby.html")
   else:
        return render_template('lobby.html')


@app.route('/registration', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        user.name, user.email, psw1, psw2 = request.form['login'], request.form['email'], request.form['psw1'], request.form['psw2']
        
        return render_template('main.html')
    return render_template('registration.html', title='Регистрация')

a, log, psw = '' , '', ''
@app.route('/log_in', methods=['POST', 'GET'])
def log_in():
    if request.method == 'POST':
        global a, log, psw
        log, psw = request.form.get('login', False), request.form.get('psw', False)
        flag = Per(log=log, pas=psw, func='check')
        if flag:
            a = Per(log=log, pas=psw, func='ret')
            return render_template('main.html')
        else:
            return render_template('log_in.html', massage='1')
    return render_template('log_in.html')


@app.route('/main', methods=['POST', 'GET'])
def main():
    global a, log, psw
    if request.method == 'POST':
        a1 = request.form['all']
        Per(log=log, pas=psw, al=a1, func='change')
        a = a1
        render_template('main.html', allergs=a)
    render_template('main.html', allergs=a)

if __name__ == '__main__':
    app.run(debug=True)