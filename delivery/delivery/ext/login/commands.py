import click
from delivery.ext.db.models import User
from delivery.ext.login.controller import create_user
from delivery.ext.db import db


@click.option("--name", "-s")
@click.option("--email", "-e")
@click.option("--password", "-p")
@click.option("--admin", "-a", is_flag=True, default=False)
def add_user(name, email, password, admin):
    """adicionando novo usuario"""
    #TODO: tratar User Exists exception
    create_user(
        name=name,
        email=email,
        password=password,
        admin=admin
    )

    click.echo(f"Usuario {email} criado com sucesso!")