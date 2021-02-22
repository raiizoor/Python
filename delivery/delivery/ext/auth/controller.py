import os, click
import cv2
import numpy as np
import warnings

from flask import redirect, url_for
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename
from flask import current_app as app
from delivery.ext.db.models import User, Category, Store, Items
from delivery.ext.db import db, models
from datetime import datetime



ALG = "pbkdf2:sha256"


def list_users():
    """Lista de usuários registrados"""
    users = models.User.query.all()
    click.echo(f"Lista de usuarios {users}")

def list_categorys():
    """Lista de categorias registradas"""
    categorys = models.Category.query.all()
    click.echo(f"Lista de categoria {categorys}")

def list_stores():
    """Lista de lojas"""
    stores = models.Store.query.all()
    click.echo(f"Lista de lojas {stores}")

def list_itens():
    """Lista de itens registrados"""
    items = models.Items.query.all()
    click.echo(f"Lista de itens {items}")

def create_user(name: str, email: str, password: str, admin:bool = False) -> User:
    user = User(
        name = name,
        email = email,
        password = generate_password_hash(password, ALG),
        admin = admin
    )
    db.session.add(user)
    db.session.commit()
    return user
    
def create_category(name: str, on_menu: bool = False) -> Category:
    category = Category(
        name = name,
        on_menu = on_menu
    )
    db.session.add(category)
    db.session.commit()
    return category

def create_store(name_store: str, user_id: Store.user, category_id: str , active: bool=True) -> Store:
    store = Store(
        name_store = name_store,
        user_id = user_id,
        category_id = category_id,
        active = active
    )
    db.session.add(store)
    db.session.commit()
    return store

def create_item(name: str, image: int, price: float, store_id: int, available: bool=True) -> Items:
    items = Items(
        name = name,
        image = image,
        price = price,
        store_id = store_id,
        available = available,
    )
    db.session.add(items)
    db.session.commit()
    return items

def save_user_picture(filename, filestore):
    filename = os.path.join(
        app.config["UPLOAD_FOLDER"],
        secure_filename(filename)
    )
    filestore.save(filename)
    imgresizer(filename)
    #TODO: 
    #1) Verificar se o diretório existe.
    #2) criar o diretório se não existir

def imgresizer(path):
    img = cv2.imread(path)
    img = cv2.resize(img,(128,128))
    path = path[0:-4]
    cv2.imwrite(path+"reduced.png",img)
# Use nesta funcao o parametro caminho absoluto
#ex: imgresizer("C:/Users/e-ron/code/Web-delivery/delivery/uploads/teste.jpg")