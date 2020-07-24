import click
from delivery.ext.db import db
from delivery.ext.db import models # noqa

def init_app(app):

    @app.cli.command()
    def create_db():
        """Este comando inicializa o db"""
        try:
            db.create_all()
        except OperationError as err:
            print("ERRO")
            print(err)

    @app.cli.command()
    @click.option("--email", "-e")
    @click.option("--passwd", "-p")
    @click.option("--admin", "-a", is_flag=True, default=False)
    def add_user(email, passwd, admin):
        """adicionando novo usuario"""
        user = models.User(
            email=email,
            passwd=passwd,
            admin=admin
        )
        db.session.add(user)
        db.session.commit()

        click.echo(f"Usuario {email} criado com sucesso!")

    @app.cli.command()
    def listar_pedidos():
        # TODO: usar tabulate
        click.echo("lista de pedidos")

    @app.cli.command()
    def listar_usuarios():
        users = models.User.query.all()
        click.echo(f"lista de usuarios {users}")
        