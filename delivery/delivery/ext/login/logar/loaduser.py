from delivery.ext.db import db
from delivery.ext.db.models import User
from werkzeug.security import generate_password_hash, check_password_hash


def __init__(self, name, email, password):
    self.name = name
    self.email = email
    self.password = generate_password_hash(password)

def verify_password(self, pwd):
    return check_password_hash(self.password, pwd)
