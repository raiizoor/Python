import wtforms as wtf
from flask_wtf import FlaskForm
from flask_wtf.file import FileField


class UserForm(FlaskForm):
    name = wtf.StringField("Nome", [wtf.validators.DataRequired()])
    email = wtf.StringField(
        "Email", [wtf.validators.DataRequired(), wtf.validators.Email()]
    )
    password = wtf.PasswordField("Senha", [wtf.validators.DataRequired()] )
    foto = FileField ("Foto")

  
class LoginForm(FlaskForm):
    email = wtf.StringField(
        "Email", [wtf.validators.DataRequired(), wtf.validators.Email()]
    )
    password = wtf.PasswordField("Senha", [wtf.validators.DataRequired()] )
"""
    confirmation = BooleanField(
        "Permanecer Conectado",
        render_kw={"class_": "uk-checkbox"},
    )
"""

class CategoryForm(FlaskForm):
    name = wtf.StringField("Nome", [wtf.validators.DataRequired()])
    onmenu = wtf.BooleanField("On-menu")
    
