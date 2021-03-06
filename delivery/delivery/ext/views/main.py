from flask import Blueprint, current_app, render_template, redirect, request, url_for, flash, send_from_directory
from flask_login import current_user, login_required, login_user
from flask_login.utils import login_required, logout_user
from delivery.ext.db import db
from delivery.ext.db.models import User
from delivery.ext.auth.form import UserForm, LoginForm
from delivery.ext.auth.controller import create_user, save_user_picture
from flask import current_app as app


main = Blueprint("main", __name__)

@main.before_request
def before_request():
    if current_user.is_authenticated:
        if request.endpoint == 'main.login':
            return redirect(url_for("page.index"))

@main.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory(app.config["UPLOAD_FOLDER"], nome_arquivo)

@main.route("/cadastro", methods=["GET", "POST"])
def signup():
    form = UserForm()

    if form.validate_on_submit():
        try:
            create_user(
                name=form.name.data,
                email=form.email.data,
                password=form.password.data,
            )
            foto = request.files.get('foto')
            if foto:
                save_user_picture(
                        foto.filename,
                        foto
                    )
            flash('Cadastrado com Sucesso! Por favor faça o login.', 'success')
            return redirect(url_for(".login"))
        except Exception:
            flash("Este email já esta cadastrado!   ", "danger")
            return redirect(url_for('.signup'))
        
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

        login_user(auth)
        return redirect(url_for('page.index'))

    return render_template('login/efectlogin.html', form=form)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.login"))

@main.route("/restaurantes")
def restaurants():
    return render_template("restaurants.html")