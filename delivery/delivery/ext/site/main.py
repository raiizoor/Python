from flask import Blueprint, current_app, render_template, redirect, request
from delivery.ext.login.form import UserForm
from delivery.ext.login.logar.form import LoginForm
from delivery.ext.login.logar.loaduser import load_user
from delivery.ext.login.controller import create_user, save_user_foto


bp = Blueprint("site", __name__)

@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/sobre")
def about():
    return render_template("about.html")

@bp.route("/cadastro", methods=["GET", "POST"])
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
        return redirect("/logado")

    return render_template("login/userform.html", form=form)

@bp.route("/entrar", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        
        load_user(
            email,
            password
        )

        flask.flash('Login feito com sucesso')

        next = flask.request.args.get('next')

        if not is_safe_url(next):
            return flask.abort(400)

        return flask.redirect(next or flask.url_for('logado.html'))
    return render_template("login/efectlogin.html", form=form)

@bp.route("/logado")
def logado():
    return render_template("login.html")

@bp.route("/restaurantes")
def restaurants():
    return render_template("restaurants.html")