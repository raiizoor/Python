import click
from delivery.ext.db.models import User, Items
from delivery.ext.auth.controller import create_user, create_category, create_store, create_item
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

@click.option("--name_store", "-s")
@click.option("--user_id", "-s")
@click.option("--category", "-s")
@click.option("--active", "-a", is_flag=True, default=True)
def add_store(name_store, user_id, category, active):
    """Adicionar nova Loja"""
    create_store(
        name_store=name_store,
        user_id=user_id,
        category=category,
        active=active
    )

    click.echo(f"Loja {name_store} criada com sucesso!")

@click.option("--name", "-s")
@click.option("--image", "-s")
@click.option("--price", "--pos")
@click.option("--store_id", "-s")
@click.option("--available", "-a")
def add_item(name, image, price, store_id, available):
    """Adicionar novo item"""
    create_item(
        name=name,
        image=image,
        price=price,
        store_id=store_id,
        available=available,
    )

    click.echo(f"Item {name} criado com sucesso!")