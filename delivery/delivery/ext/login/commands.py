import click
from delivery.ext.db import db
from delivery.ext.db import models

def list_users():
    users = models.User.query.all()
    click.echo(f"lista de usuarios {users}")
    

@click.option("--email", "-e")
@click.option("--password", "-p")
@click.option("--admin", "-a", is_flag=True, default=False)
def add_user(email, password, admin):
    """adicionando novo usuario"""
    user = models.User(
        email=email,
        password=password,
        admin=admin
    )
    db.session.add(user)
    db.session.commit()

    click.echo(f"Usuario {email} criado com sucesso!")