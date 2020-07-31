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
    def listar_pedidos():
        # TODO: usar tabulate
        click.echo("lista de pedidos")
        