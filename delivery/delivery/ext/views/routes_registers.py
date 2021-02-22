from flask import Blueprint, render_template, redirect, url_for, flash  
from flask_login import login_required
from delivery.ext.auth.form import CategoryForm, ItemsForm, StoresForm, AddressForm, OrderItemsForm
from delivery.ext.auth.controller import create_category, create_item, create_store

category = Blueprint("cate", __name__)

@category.route('/')
@category.route('/page')
@login_required
def page():
    return render_template('login.html')


@category.route('/categoria', methods=['GET', 'POST'])
@login_required
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
            flash('Essa categoria já existe, registre outra!', 'warning')
            return redirect(url_for('.register_category'))

    return render_template("categoria.html", cate=cate)


@category.route('/loja', methods=['GET', 'POST'])
@login_required
def register_store():
    store = StoresForm()

    if store.validate_on_submit():
        create_store(
            name_store=name_store,
            user_id=user_id,
            category_id=category_id,
            active=active
        )
        return redirect(url_for('.register_store'))

    return render_template("stores.html", store=store)


@category.route('/items', methods=['GET', 'POST'])
@login_required
def register_items():
    item = ItemsForm()

    if item.validate_on_submit():  
        create_item(
            name=item.name.data,
            image=item.image.data,
            price=item.price.data,
            store_id=item.store_id.data,
            available=item.available.data,
        )
        flash('Item registrado com sucesso!', 'success')
        return redirect(url_for('.register_items'))

    return render_template("items.html", item=item)

@category.route('/address', methods=['GET', 'POST'])
@login_required
def register_address():
    address = AddressForm()

    return render_template("address.html", address=address)

@category.route('/order_items', methods=['GET', 'POST'])
@login_required
def register_order_items():
    order_items = OrderItemsForm()

    return render_template("order_items.html", order_items=order_items)