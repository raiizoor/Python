import click
from delivery.ext.db.models import User, Items
from delivery.ext.auth.controller import create_user, create_category, create_store, create_item, create_address
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
@click.option("--category_id", "-s")
@click.option("--active", "-a", is_flag=True, default=False)
def add_store(name_store, user_id, category_id, active):
    """Adicionar nova Loja"""
    create_store(
        name_store=name_store,
        user_id=user_id,
        category_id=category_id,
        active=active
    )

    click.echo(f"Loja {name_store} criada com sucesso!")

@click.option("--name", "-s")
@click.option("--image", "-s")
@click.option("--price", "--pos")
@click.option("--store_id", "-s")
@click.option("--available", "-a", is_flag=True, default=True)
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


@click.option("--zip", "-s")
@click.option("--state", "-s")
@click.option("--city", "-s")
@click.option("--address", "-s")
@click.option("--number_house", "--n")
def add_address(zip, state, city, address, number_house):
    """Adicionar novo endereço"""
    create_address(
        zip=zip,
        state=state,
        city=city,
        address=address,
        number_house=number_house,
    )

    click.echo(f"Endereço {address} criado com sucesso!")
