from delivery.ext.db import models #noqa
from delivery.ext.login.commands import list_users, add_user

from delivery.ext.db import db
from delivery.ext.login.admin import UserAdmin
from delivery.ext.admin import admin
from delivery.ext.db.models import User

def init_app(app):
    app.cli.command()(list_users)
    app.cli.command()(add_user)

    admin.add_view(UserAdmin(User, db.session))