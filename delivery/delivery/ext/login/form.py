import wtforms as wtf
from flask_wtf import FlaskForm
from flask_wtf.file import FileField


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

class ItemsForm(FlaskForm):
    name = wtf.StringField("Nome", [wtf.validators.DataRequired()])
    image = FileField("Image", [wtf.validators.DataRequired()])
    price = wtf.FloatField("Preço", [wtf.validators.DataRequired()])
    manysold = wtf.IntegerField("ManySold", [wtf.validators.DataRequired()])
    dateadded = wtf.DateTimeField("DateAdded", [wtf.validators.DataRequired()])

    

class CategoryForm(FlaskForm):
    name = wtf.StringField("Nome", [wtf.validators.DataRequired()])
    onmenu = wtf.BooleanField("On-menu")
