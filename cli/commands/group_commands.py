import click
from . import handle_errors
from cli.templates.models import server_model
import logging

logger = logging.getLogger(__name__)


@click.group(name="group")
def group_cli():
    """Группа команд для работы с группами."""
    pass



@handle_errors()
@group_cli.command()
@click.option('--name', help="Название группы.")
def start(name):
    """Приветствие пользователя с учетом возраста."""
    if age < 18:
        click.secho(f"Привет, {name}! Ты молод!", fg="cyan")
    else:
        click.secho(f"Привет, {name}! Добро пожаловать!", fg="yellow")

    logger.info(f"Приветствие отправлено для пользователя: {name}, возраст: {age}")
