import click
from delivery.ext.db.models import User, Items
from delivery.ext.auth.controller import create_user, create_category, create_store, create_item, create_address, create_order
from delivery.ext.db import db
from datetime import datetime


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
@click.option("--on_menu", "-a", is_flag=True, default=True)
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
@click.option("--price", "--pos")
@click.option("--store_id", "-s")
@click.option("--available", "-a", is_flag=True, default=True)
def add_item(name, price, store_id, available):
    """Adicionar novo item"""
    create_item(
        name=name,
        price=price,
        store_id=store_id,
        available=available,
    )

    click.echo(f"Item {name} criado com sucesso!")


@click.option("--zip_code", "-s")
@click.option("--state", "-s")
@click.option("--city", "-s")
@click.option("--address", "-s")
@click.option("--number_house", "--n")
@click.option("--user_id", "-s")
def add_address(zip_code, state, city, address, number_house, user_id):
    """Adicionar novo endereço"""
    create_address(
        zip_code=zip_code,
        state=state,
        city=city,
        address=address,
        number_house=number_house,
        user_id=user_id
    )

    click.echo(f"Endereço {address} criado com sucesso!")

#a= datetime.now()
#b = a.strftime("%d-%m-%Y, %H:%M:%S")
@click.option("--created_at", "-s")
@click.option("--completed", "-a",is_flag=True, default=True)
@click.option("--user_id", "-s")
@click.option("--store_id", "-s")
def add_order(created_at, completed, user_id, store_id):
    """Adicionar nova ordem de compra"""
    create_order(
        created_at=datetime.now(),
        completed=completed,
        user_id=user_id,
        store_id=store_id
    )

    click.echo(f"Endereço {user_id} criado com sucesso!")