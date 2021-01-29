from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required
from delivery.ext.login.form import CategoryForm
from delivery.ext.login.controller import create_category

category = Blueprint("cate", __name__)

@category.route('/page')
@login_required
def page():
    return render_template('login.html')

@category.route('/categoria', methods=['GET', 'POST'])
def register():
    cate = CategoryForm()

    if cate.validate_on_submit():
        create_category(
            name=cate.name.data,
            onmenu=cate.onmenu.data,
        )
        
        return redirect(url_for('.register'))

    return render_template("categoria.html", cate=cate)