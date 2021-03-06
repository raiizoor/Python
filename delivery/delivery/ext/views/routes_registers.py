from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask import current_app as app
from flask_login import login_required, current_user
from delivery.ext.auth.form import CategoryForm, ItemsForm, StoresForm, AddressForm, OrderForm, OrderItemsForm
from delivery.ext.auth.controller import create_category, create_item, create_store, create_address, create_order, save_user_picture, del_category
from datetime import datetime
from delivery.ext.db.models import Category, Store, Items, Address, Order, OrderItems

category = Blueprint("cate", __name__)

@category.route('/')
@category.route('/page')
@login_required
def page():
    return render_template('login.html')

@category.route('/lista_categoria', methods=['GET', 'POST'])
@login_required
def list_category():
    categorys = Category.query.all()
    return render_template('category/list_category.html', categorys=categorys)

@category.route('/categoria', methods=['GET', 'POST'])
@login_required
def register_category():
    form = CategoryForm()

    if form.validate_on_submit():  
        try:
            create_category(
                name=form.name.data,
                on_menu=form.on_menu.data
            )
            flash('Categoria registrada com sucesso!', 'success')
            return redirect(url_for('.register_category'))
        except Exception:
            flash('Essa categoria já existe, registre outra!', 'warning')
            return redirect(url_for('.register_category'))

    return render_template("category/register_category.html", form=form)

@category.route('/editar_categoria', methods=['GET', 'POST'])
@login_required
def edit_category():
    

    return render_template('category/edit_category.html')

@category.route('/deletar_categoria')
@login_required
def delete_category(id):
    del_category(id)
    flash('categoria deletada!')
    return redirect(url_for('.list_category'))

@category.route('/lista_loja', methods=['GET', 'POST'])
@login_required
def list_store():
    stores = Store.query.all()
    return render_template('store/list_store.html', stores=stores)

@category.route('/deletar_loja', methods=['GET', 'POST'])
@login_required
def delete_store():
    pass

@category.route('/editar_loja', methods=['GET', 'POST'])
@login_required
def edit_store():

    return render_template('store/edit_store.html')

@category.route('/loja', methods=['GET', 'POST'])
@login_required
def register_store():
    form = StoresForm()

    if form.validate_on_submit():
        try:
            create_store(
                name_store=form.name_store.data,
                user_id=current_user.email,
                category_id=form.category_id.data,
                active = form.active.data
            )
            flash('Estabelecimento registrado com sucesso!', 'success')
            return redirect(url_for('.register_store'))
        except Exception:
            flash('Esse estabelecimento já foi registrado. Cadastre outro!', 'warning')
            return redirect(url_for('.register_store'))

    return render_template("store/register_store.html", form=form)

@category.route('/lista_itens', methods=['GET', 'POST'])
@login_required
def list_items():
    item = Items.query.all()
    return render_template('items/list_items.html', item=item)

@category.route('/editar_itens', methods=['GET', 'POST'])
@login_required
def edit_items():

    return render_template('items/edit_items.html')

@category.route('/editar_itens', methods=['GET', 'POST'])
@login_required
def delete_items():
    pass

@category.route('/items', methods=['GET', 'POST'])
@login_required
def register_items():
    form = ItemsForm()

    if form.validate_on_submit(): 
        try:  
            create_item(
                name=form.name.data,
                price=form.price.data,
                store_id=form.store_id.data,
                available=form.available.data,
            )
            image = request.files.get('image')
            if image:
                save_user_picture(
                        image.filename,
                        image
                    )

            flash('Item registrado com sucesso!', 'success')
            return redirect(url_for('.register_items'))
        except Exception:
            flash('deu ruim', 'danger')
            return redirect(url_for('.register_items'))

    return render_template("items/register_items.html", form=form)

@category.route('/lista_endereço', methods=['GET', 'POST'])
@login_required
def list_address():
    addresses = Address.query.all()
    return render_template('address/list_address.html', addresses=addresses)

@category.route('/editar_endereço', methods=['GET', 'POST'])
@login_required
def edit_address():

    return render_template('address/edit_address.html')

@category.route('/deletar_endereço', methods=['GET', 'POST'])
@login_required
def delete_address():
    pass

@category.route('/endereço', methods=['GET', 'POST'])
@login_required
def register_address():
    form = AddressForm()
    
    if form.validate_on_submit():
        try:
            create_address(
                zip_code=form.zip_code.data,
                state=form.state.data,
                city=form.city.data,
                address=form.address.data,
                number_house=form.number_house.data,
                user_id=current_user.email
            )
            flash('Endereço registrado com sucesso!', 'success')
            return redirect(url_for('.register_address'))
        except Exception:
            flash('Algo deu errado tente novamente!','warning')
            return redirect(url_for('.register_address'))

    return render_template("address/register_address.html", form=form)

@category.route('/lista_ordem', methods=['GET', 'POST'])
@login_required
def list_order():
    orders = Order.query.all()
    return render_template('order/list_order.html', orders=orders)

@category.route('/editar_ordem', methods=['GET', 'POST'])
@login_required
def edit_order():

    return render_template('order/edit_order.html')

@category.route('/deletar_ordem', methods=['GET', 'POST'])
@login_required
def delete_order():
    pass

@category.route('/ordem', methods=['GET', 'POST'])
@login_required
def register_order():
    form = OrderForm()
    
    if form.validate_on_submit():
        try:
            create_order(
                created_at=datetime.now(),
                completed=form.completed.data,
                user_id=current_user.email,
                store_id=form.store_id.data,
            )
            flash('Ordem de compra registrada com sucesso!', 'success')
            return redirect(url_for('.register_order'))
        except Exception:
            flash('Algo deu errado tente novamente!','warning')
            return redirect(url_for('.register_order'))

    return render_template("order/register_order.html", form=form)

@category.route('/lista_order_itens', methods=['GET', 'POST'])
@login_required
def list_order_items():
    order_item = OrderItems.query.all()
    return render_template('order_items/list_order_items.html', order_item=order_item)

@category.route('/editar_order_itens', methods=['GET', 'POST'])
@login_required
def edit_order_items():

    return render_template('order_items/edit_order_items.html')

@category.route('/deletar_order_itens', methods=['GET', 'POST'])
@login_required
def delete_order_items():
    pass

@category.route('/ordem_itens', methods=['GET', 'POST'])
@login_required
def register_order_items():
    form = OrderItemsForm()

    return render_template("order_items/register_order_items.html", form=form)