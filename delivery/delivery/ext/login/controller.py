import os, click
import cv2
import numpy as np

from flask import flash, redirect, url_for
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename
from flask import current_app as app
<<<<<<< HEAD
from delivery.ext.db.models import User, Items, Store
=======
from delivery.ext.db.models import User, Category
from delivery.ext.db.models import User, Items
>>>>>>> 5244b5f7d648bf51311bf3090c90691484c6c5c8
from delivery.ext.db import db, models



ALG = "pbkdf2:sha256"


def list_users():
    users = models.User.query.all()
    click.echo(f"lista de usuarios {users}")

def create_category(name: str, onmenu:bool = False) -> Category:
    category = Category(
        name = name,
        onmenu = onmenu
    )
    db.session.add(category)
    db.session.commit()
    return category

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

def create_item(name: str, image: str, price: int) -> Items:
    items = Items(
        name = name,
        image = image,
        price = price
    )
    db.session.add(items)
    #TODO: Tratar exception caso o item já exista
    db.session.commit()
    return items

def save_user_foto(filename, filestore):
    filename = os.path.join(
        app.config["UPLOAD_FOLDER"],
        secure_filename(filename)
    )
    filestore.save(filename)
    imgresizer(filename)

def imgresizer(path):
    img = cv2.imread(path)
    img = cv2.resize(img,(128,128))
    path = path[0:-4]
    cv2.imwrite(path+"reduced.png",img)
# Use nesta funcao o parametro caminho absoluto
#ex: imgresizer("C:/Users/e-ron/code/Web-delivery/delivery/delivery/uploads/teste.jpg")