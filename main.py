from flask import Flask, render_template, request, redirect, url_for
from data.base import Per
from photo import found
from flask_login import LoginManager, login_user
import os

SECRET_KEY = os.urandom(32)


app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY


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
        log, em, psw1, psw2 = request.form['login'], request.form['email'], request.form['psw1'], request.form['psw2']
        Per(log=log, em=em, pas=psw1, func='creat')
        return render_template('main.html')
    return render_template('registration.html', title='Регистрация')

log, psw = '', ''
@app.route('/log_in', methods=['POST', 'GET'])
def log_in():
    if request.method == 'POST':
        global log, psw
        log, psw = request.form['login'], request.form['psw']
        flag = Per(log=log, pas=psw, func='check')
        if flag:
            return render_template('main.html')
        else:
            return render_template('log_in.html', massage='1')
    return render_template('log_in.html')

@app.route('/main', methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        a = request.form['all']
        Per(log=log, pas=psw, al=a, func='change')
        render_template('main.html', allergs=a)
    render_template('main.html', allergs=Per(log=log, pas=psw, func='ret'))

if __name__ == '__main__':
    app.run(debug=True)