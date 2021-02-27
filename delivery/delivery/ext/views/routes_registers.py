from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from delivery.ext.auth.form import CategoryForm, ItemsForm, StoresForm, AddressForm, OrderForm, OrderItemsForm
from delivery.ext.auth.controller import create_category, create_item, create_store, create_address, create_order, save_user_picture
from datetime import datetime

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
        try:
            create_store(
                name_store=store.name_store.data,
                user_id=current_user.email,
                category_id=store.category_id.data,
                active = store.active.data
            )
            flash('Estabelecimento registrado com sucesso!', 'success')
            return redirect(url_for('.register_store'))
        except Exception:
            flash('Esse estabelecimento já foi registrado. Cadastre outro!', 'warning')
            return redirect(url_for('.register_store'))

    return render_template("stores.html", store=store)


@category.route('/items', methods=['GET', 'POST'])
@login_required
def register_items():
    item = ItemsForm()

    if item.validate_on_submit():  
        create_item(
            name=item.name.data,
            price=item.price.data,
            store_id=item.store_id.data,
            available=item.available.data,
        )
        imagem = request.files.get('imagem')
        if imagem:
            save_user_picture(
                imagem.filename,
                imagem
            )
        flash('Item registrado com sucesso!', 'success')
        return redirect(url_for('.register_items'))

    return render_template("items.html", item=item)

@category.route('/address', methods=['GET', 'POST'])
@login_required
def register_address():
    addres = AddressForm()
    
    if addres.validate_on_submit():
        try:
            create_address(
                zip_code=addres.zip_code.data,
                state=addres.state.data,
                city=addres.city.data,
                address=addres.address.data,
                number_house=addres.number_house.data,
                user_id=current_user.email
            )
            flash('Endereço registrado com sucesso!', 'success')
            return redirect(url_for('.register_address'))
        except Exception:
            flash('Algo deu errado tente novamente!','warning')
            return redirect(url_for('.register_address'))

    return render_template("address.html", addres=addres)

@category.route('/order', methods=['GET', 'POST'])
@login_required
def register_order():
    order = OrderForm()
    
    if order.validate_on_submit():
        try:
            create_order(
                created_at=datetime.now(),
                completed=order.completed.data,
                user_id=current_user.email,
                store_id=order.store_id.data,
            )
            flash('Ordem de compra registrada com sucesso!', 'success')
            return redirect(url_for('.register_order'))
        except Exception:
            flash('Algo deu errado tente novamente!','warning')
            return redirect(url_for('.register_order'))

    return render_template("order.html", order=order)



@category.route('/order_items', methods=['GET', 'POST'])
@login_required
def register_order_items():
    order_items = OrderItemsForm()

    return render_template("order_items.html", order_items=order_items)