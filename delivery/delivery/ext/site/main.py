from flask import render_template
from flask import Blueprint
from delivery.ext.login.form import UserForm

bp = Blueprint("site", __name__)

@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/sobre")
def about():
    return render_template("about.html")

@bp.route("/cadastro")
def signup():
    form = UserForm()
    return render_template("userform.html", form=form)

@bp.route("/restaurantes")
def restaurants():
    return render_template("restaurants.html")