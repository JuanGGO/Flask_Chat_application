from app.auth import auth
from flask_login import login_user
from flask import render_template, flash, redirect, url_for
from .forms import LoginForm, RegisterForm
from app.models import User
from app import db


@auth.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.verify_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for("main.index"))
        return render_template('error.html', message="username or password invalid")

    return render_template("auth/login.html", form=form)


@auth.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash("You are registered!")
        return redirect(url_for('auth.login'))

    return render_template("auth/register.html", form=form)
