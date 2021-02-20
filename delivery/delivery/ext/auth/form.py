import wtforms as wtf
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from delivery.ext.db.models import Store, User, Category
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


class StoreForm(FlaskForm):
    name_store = wtf.StringField("Nome da Loja", [wtf.validators.DataRequired()])
    user_id = QuerySelectField(querry_factory=lambda: User.query.all())
    category_id = QuerySelectField(querry_factory=lambda: Category.query.all())
    active = wtf.BooleanField("Ativar", default=False)


class ItemsForm(FlaskForm):
    name = wtf.StringField("Nome", [wtf.validators.DataRequired()])
    image = FileField("Image")
    price = wtf.FloatField("Preço", [wtf.validators.DataRequired()])
    store_id = QuerySelectField('store_id', query_factory=lambda: Store.query.all())
    available = wtf.BooleanField("Disponivel", default=True)

    #def possible_id_store():
     #   return Store.query.with_entities(Store.id)

