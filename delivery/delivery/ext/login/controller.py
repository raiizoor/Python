import os, click
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
    """
    Saves user foto in
    ./uploads/foo/fasgyda.ext
    """
    
    filename = os.path.join(
        app.config["UPLOAD_FOLDER"],
        secure_filename(filename)
    ) 
    # TODO:
    # 1) verificar se o dir existe
    # 2)criar o diretorio
    filestore.save(filename)