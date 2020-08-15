from flask import Blueprint, current_app, render_template, redirect, request
from delivery.ext.login.form import UserForm
from delivery.ext.login.controller import create_user

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
        
        #forçar login
        return redirect("/")

    return render_template("userform.html", form=form)

@bp.route("/restaurantes")
def restaurants():
    return render_template("restaurants.html")