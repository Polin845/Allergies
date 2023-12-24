from flask import Flask, render_template, request, redirect, session, abort
from data import dase
from data.users import User
from Forms.log_in import LoginForm
from Forms.register import RegisterForm
from Forms.index import AllergensForm
from Forms.Photo import PhotoForm
from flask_login import login_user, LoginManager
from photo import found
import os

SECRET_KEY = os.urandom(32)
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

dase.global_init("db/blogs.db")

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    db_sess = dase.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/registration', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('registration.html', title='Регистрация', form=form, message="Пароли не совпадают")
        db_sess = dase.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('registration.html', title='Регистрация', form=form, message="Такой пользователь уже есть")
        user = User(email=form.email.data)
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/')
    return render_template('registration.html', title='Регистрация', form=form)


@app.route('/', methods=['POST', 'GET'])
def log_in():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = dase.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect(f'/main/{user.id}')
        return render_template('log_in.html', message="Неправильный логин или пароль", form=form)
    return render_template('log_in.html', title='Авторизация', form=form)


@app.route('/main/<id>', methods=['POST', 'GET'])
def main(id):
    form = AllergensForm()
    db_sess = dase.create_session()
    user = db_sess.query(User).filter(User.id == id).first()
    if not user:
        abort(401)
    if session['_user_id'] != str(user.id):
        abort()
    if request.method == 'POST':
        if request.values['change'] == 'Изменить':
            user.allergens = form.allergs.data
            db_sess.merge(user)
            db_sess.commit()
            print(request.form)
        else:
            form = PhotoForm()
            al = user.allergens
            image = form.file.data
            flag = found(image, al)
            if flag != []:
                return render_template('main.html', flag=flag, allergs=user.allergens)
            return render_template('main.html', allergs=user.allergens, ok='Всё хорошо')
    return render_template('main.html', form=form, alergs=user.allergens)


if __name__ == '__main__':
    app.run(debug=True)