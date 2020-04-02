from app.main import main
from flask import render_template, redirect, url_for
from flask_login import current_user
from app.models import User


@main.route("/")
def index():
    if current_user.is_authenticated:
        return redirect(url_for('main.chat', username=current_user.username))
    return redirect(url_for('auth.login'))

@main.route("/<string:username>")
def chat(username):
    user = User.query.filter_by(username=username).first()
    if current_user.id == user.id:
        return render_template("main/chat.html", user=user)
    else:
        return render_template("error.html", message="The url requested does not exists")


