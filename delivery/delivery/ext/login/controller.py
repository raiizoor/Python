import os
from werkzeug.security import generate_password_hash

from werkzeug.utils import secure_filename

from flask import current_app as app

from delivery.ext.db.models import User
from delivery.ext.db import db


ALG = "pbkdf2:sha256"


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
        app.config
    ) 
    filestore.save(secure_filename(filename))