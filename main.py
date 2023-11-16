from flask import Flask, render_template
from data.base import Log
from flask_login import LoginManager, login_user

app = Flask(__name__)

@app.route('/')
def ajr():
    return render_template('a.html')

@app.route('/log_on')
def loginig():
    return render_template('l_on.html')



