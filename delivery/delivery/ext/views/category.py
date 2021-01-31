from flask import Blueprint, render_template, redirect, url_for, flash  
from flask_login import login_required
from delivery.ext.login.form import CategoryForm, ItemsForm
from delivery.ext.login.controller import create_category

category = Blueprint("cate", __name__)

@category.route('/page')
def page():
    return render_template('login.html')

@category.route('/items', methods=['GET', 'POST'])
def register_items():
    item = ItemsForm()

    return render_template("items.html", item=item)

@category.route('/categoria', methods=['GET', 'POST'])
def register_category():
    cate = CategoryForm()

    if cate.validate_on_submit():  
        try:
            create_category(
                name=cate.name.data,
            )
            flash('Categoria registrada com sucesso!', 'success')
            return redirect(url_for('.register_category'))
        except Exception:
            flash('Categoria já existe, registre outra!', 'warning')
            return redirect(url_for('.register_category'))


    return render_template("categoria.html", cate=cate)