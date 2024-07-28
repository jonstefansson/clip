import sys
import click
from clip.ui.clipboard import ClipboardApp
from PySide6.QtWidgets import QApplication
from .tools.table_reader import TableReader


@click.group()
def cli():
    pass


@cli.command('run')
@click.argument('data_input', required=False, type=click.File('rt'))
def run(data_input):
    data = TableReader.read(data_input)
    app = QApplication(sys.argv)
    ex = ClipboardApp(data)
    sys.exit(app.exec_())


@cli.command('read')
@click.argument('data_input', required=True, type=click.File('rt'))
def read(data_input):
    from icecream import ic
    ic(TableReader.read(data_input))


if __name__ == "__main__":
    cli()
