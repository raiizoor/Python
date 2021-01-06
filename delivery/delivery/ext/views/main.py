from flask import Blueprint, current_app, render_template, redirect, request, url_for, flash
from flask_login import login_user, current_user
from delivery.ext.db import db
from delivery.ext.db.models import User
from delivery.ext.login.form import UserForm
from delivery.ext.login.logar.form import LoginForm
from delivery.ext.login.controller import create_user, save_user_foto


main = Blueprint("main", __name__)

@main.before_request
def before_request():
    if current_user.is_authenticated:
        if request.endpoint == "auth.login":
            return redirect(url_for("dashboard.page"))

@main.route("/cadastro", methods=["GET", "POST"])
def signup():
    form = UserForm()

    if form.validate_on_submit():
        create_user(
            name=form.name.data,
            email=form.email.data,
            password=form.password.data,
        )
        foto = request.files.get('foto')
        if foto:
            save_user_foto(
                    foto.filename,
                    foto
                )
        #forçar login
        return redirect(url_for('.logado'))

    return render_template("login/userform.html", form=form)


@main.route("/entrar", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User()
        auth = user.auth(form.email.data, form.password.data)

        if not auth:
            flash("suas credênciais estão incorretas!", "danger")
            return redirect(url_for('.login'))

        return redirect(url_for(".logado"))

    return render_template('login/efectlogin.html', form=form)


@main.route("/logado")
def logado():
    return render_template("login.html")

@main.route("/restaurantes")
def restaurants():
    return render_template("restaurants.html")