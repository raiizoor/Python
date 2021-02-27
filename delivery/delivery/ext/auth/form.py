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


def category_query():
    return Category.query

def user_query():
    return User.query

class StoresForm(FlaskForm):
    name_store = wtf.StringField("Nome da Loja", [wtf.validators.DataRequired()])
    #category_id = QuerySelectField(query_factory=category_query, allow_blank=False, get_label='name')
    category_id = wtf.StringField("Categoria", [wtf.validators.DataRequired()])
    active = wtf.BooleanField("Ativo", default=True)

class ItemsForm(FlaskForm):
    name = wtf.StringField("Nome", [wtf.validators.DataRequired()])
    imagem = FileField("Imagem")
    price = wtf.FloatField("Preço", [wtf.validators.DataRequired()])
    #store_id = QuerySelectField('store_id', query_factory=lambda: Store.query.all())
    store_id = wtf.StringField("Loja",[wtf.validators.DataRequired()])
    available = wtf.BooleanField("Disponivel", default=True)

class AddressForm(FlaskForm):
    zip_code = wtf.StringField("CEP", [wtf.validators.DataRequired()])
    state = wtf.StringField("Estado")               
    city = wtf.StringField("Cidade")                
    address= wtf.StringField("Endereço", [wtf.validators.DataRequired()])
    number_house= wtf.IntegerField("N°", [wtf.validators.DataRequired()])

class OrderForm(FlaskForm):
    created_at = wtf.StringField("Data e Hora")
    completed = wtf.BooleanField("Comprado")
    store_id = wtf.StringField("Loja", [wtf.validators.DataRequired()])

class OrderItemsForm(FlaskForm):
    order_id = QuerySelectField("order_id", query_factory=lambda: Order.query.all())
    items_id = QuerySelectField("items_id", query_factory=lambda: Items.query.all())
    quant = wtf.IntegerField("Quantidade", [wtf.validators.DataRequired()])
