import os, click
import cv2
import numpy as np

from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename
from flask import current_app as app
from delivery.ext.db.models import User
from delivery.ext.db import db, models



ALG = "pbkdf2:sha256"


def list_users():
    users = models.User.query.all()
    click.echo(f"lista de usuarios {users}")

def create_user(name: str, email: str, password: str, admin:bool = False) -> User:
    user = User(
        name = name,
        email=email,
        password = generate_password_hash(password, ALG),
        admin = admin
    )
    db.session.add(user)
    #TODO: Tratar exception caso o usuario já exista
    db.session.commit()
    return user

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