from delivery.ext.db import models #noqa
from delivery.ext.login.commands import add_user, add_category, add_store, add_item
from delivery.ext.login.controller import list_users, list_categorys, list_store, list_items

from delivery.ext.db import db
from delivery.ext.login.admin import UserAdmin
from delivery.ext.admin import admin
from delivery.ext.db.models import User

def init_app(app):
    app.cli.command()(list_users)
    app.cli.command()(list_categorys)
    app.cli.command()(list_store)
    app.cli.command()(list_items)
    app.cli.command()(add_user)
    app.cli.command()(add_category)
    app.cli.command()(add_store)
    app.cli.command()(add_item)

    admin.add_view(UserAdmin(User, db.session))