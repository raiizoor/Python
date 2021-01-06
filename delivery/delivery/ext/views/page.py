from flask import Blueprint, render_template


page = Blueprint("page", __name__)

@page.route("/")
def index():
    return render_template("index.html")

@page.route("/restaurantes")
def restaurants():
    return render_template("restaurants.html")

@page.route("/sobre")
def about():
    return render_template("about.html")
