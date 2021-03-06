from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from delivery.ext.db import db
from delivery.ext.db.models import Category
from delivery.ext.db.models import Store
from delivery.ext.db.models import Items
from delivery.ext.db.models import Order
from delivery.ext.db.models import OrderItems
from delivery.ext.db.models import Checkout
from delivery.ext.db.models import Address


admin = Admin()

def init_app(app):
    admin.name = "CodeFoods"
    admin.template_mode = "bootstrap2"
    admin.init_app(app)

    admin.add_view(ModelView(Category, db.session))
    admin.add_view(ModelView(Store, db.session))
    admin.add_view(ModelView(Items, db.session))
    admin.add_view(ModelView(Order, db.session))
    admin.add_view(ModelView(OrderItems, db.session))   
    admin.add_view(ModelView(Checkout, db.session))   
    admin.add_view(ModelView(Address, db.session))   