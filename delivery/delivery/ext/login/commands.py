import click
from delivery.ext.db.models import User, Items
from delivery.ext.login.controller import create_user, create_category, create_item
from delivery.ext.db import db


@click.option("--name", "-s")
@click.option("--email", "-e")
@click.option("--password", "-p")
@click.option("--admin", "-a", is_flag=True, default=False)
def add_user(name, email, password, admin):
    """Adicionando novo usuario"""
    try:
        create_user(
            name=name,
            email=email,
            password=password,
            admin=admin
        )
        click.echo(f"Usuario {email} criado com sucesso!")
    except Exception:
        click.echo("Usuário já existe!")

@click.option("--name", "-s")
@click.option("--on_menu", "-a", is_flag=True, default=False)
def add_category(name, on_menu):
    """Adicionando nova categoria"""
    try:
        create_category(
            name=name,
            on_menu=on_menu
        )
        click.echo(f"Categoria {name} criada com sucesso!")
    except Exception:
        click.echo("Categoria já existe!")


@click.option("--name", "-s")
@click.option("--image", "-s")
@click.option("--price", "-f")
@click.option("--store_id", "-s")
@click.option("--manysold", "-i")
@click.option("--dateadded", "-s")
def add_item(name, image, price, store_id, manysold, dateadded):
    """Adicionar novo item"""
    create_item(
        name=name,
        image=image,
        price=price,
        store_id=store_id,
        manysold=manysold,
        dateadded=dateadded
    )

    click.echo(f"Usuario {name} criado com sucesso!")