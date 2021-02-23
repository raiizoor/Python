import wtforms as wtf
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from delivery.ext.db.models import Store, User, Category, Address, OrderItems, Order, Items
from wtforms.ext.sqlalchemy.fields import QuerySelectField

class UserForm(FlaskForm):
    name = wtf.StringField("Nome", [wtf.validators.DataRequired()])
    email = wtf.StringField("Email", [wtf.validators.DataRequired(), wtf.validators.Email()])
    password = wtf.PasswordField("Senha", [wtf.validators.DataRequired()] )
    foto = FileField ("Foto")


class LoginForm(FlaskForm):
    email = wtf.StringField(
        "Email", [wtf.validators.DataRequired(), wtf.validators.Email()]
    )
    password = wtf.PasswordField("Senha", [wtf.validators.DataRequired()] )


class CategoryForm(FlaskForm):
    name = wtf.StringField("Nome", [wtf.validators.DataRequired()])
    onmenu = wtf.BooleanField("On-menu")


class StoresForm(FlaskForm):
    name_store = wtf.StringField("Nome da Loja", [wtf.validators.DataRequired()])
    user_id = QuerySelectField("user_id", query_factory=lambda: User.query.all(), get_label='email')
    category_id = QuerySelectField(query_factory=lambda: Category.query.all(), get_label='name')

class ItemsForm(FlaskForm):
    name = wtf.StringField("Nome", [wtf.validators.DataRequired()])
    image = FileField("Image")
    price = wtf.FloatField("Preço", [wtf.validators.DataRequired()])
    store_id = QuerySelectField('store_id', query_factory=lambda: Store.query.all())
    available = wtf.BooleanField("Disponivel", default=True)

class AddressForm(FlaskForm):
    zip = wtf.StringField("CEP", [wtf.validators.DataRequired()])
    state = wtf.SelectField("Estado")               
    city = wtf.SelectField("Cidade")               
    address= wtf.StringField("Endereço", [wtf.validators.DataRequired()])
    number_house= wtf.IntegerField("N°", [wtf.validators.DataRequired()])

class OrderItemsForm(FlaskForm):
    order_id = QuerySelectField("order_id", query_factory=lambda: Order.query.all())
    items_id = QuerySelectField("items_id", query_factory=lambda: Items.query.all())
    quant = wtf.IntegerField("Quantidade", [wtf.validators.DataRequired()])
