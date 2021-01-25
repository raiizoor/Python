from flask import Blueprint, current_app, render_template, redirect, request, url_for, flash, send_from_directory
from flask_login import login_user, current_user
from flask_login.utils import login_required, logout_user
from delivery.ext.db import db
from delivery.ext.db.models import User
from delivery.ext.login.form import UserForm
from delivery.ext.login.logar.form import LoginForm
from delivery.ext.login.controller import create_user, save_user_foto
from flask import current_app as app


main = Blueprint("main", __name__)

@main.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory(app.config["UPLOAD_FOLDER"], nome_arquivo)

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
        return render_template("login.html")

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

        return render_template("login.html")

    return render_template('login/efectlogin.html', form=form)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("page.index"))

@main.route("/restaurantes")
def restaurants():
    return render_template("restaurants.html")