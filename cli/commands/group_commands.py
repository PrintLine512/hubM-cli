import logging
import subprocess
import sys

import click

from models import Servers
from . import handle_work

logger = logging.getLogger(__name__)

#@handle_work
@click.group(name="group")
@click.argument("group_name")
@click.pass_context
def group_cli(ctx, group_name):
    """Группа команд для работы с группами."""
    ctx.obj['NAME'] = group_name  # Сохраняем значение параметра `name` в контексте




@handle_work
@group_cli.command()
@click.option('--name', help="Название группы.")
def start(name):
    """Приветствие пользователя с учетом возраста."""
    try:
        subprocess.run([ "HUB-CORE", "-b", "-c", "/usr/local/etc/virtualhere/groups/Test.ini"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        logger.info(f"Приветствие отправлено для пользователя: {name}, возраст: ")
        sys.exit()
    except Exception as e:
        logger.critical(e)
        sys.exit(1)


@group_cli.command()
@handle_work
@click.option('--tcp-port', show_default=True, help="TCP-порт для подключения к базе данных.", prompt = ("Введите порт"))
def con(ctx, session, tcp_port):
    """Crонфигуровать сервер"""
    name = ctx.obj.get('NAME')  # Получаем значение `name` из контекста

    server = session.query(Servers).filter_by(name=name).first()
    if server is None:
        raise FileNotFoundError(f"Сервер '{name}' не найден.")
        click.secho(f"Группа \"{name}\" не найдена!", fg="red")
        sys.exit(1)
    print(server.tcp_port)
    server.tcp_port = tcp_port
    session.commit()
    print(name, tcp_port)


@group_cli.command()
@handle_work
def show(ctx, session):
    """Текущая конфигурация сервера"""
    name = ctx.obj.get('NAME')  # Получаем значение `name` из контекста

    server = session.query(Servers).filter_by(name=name).first()
    if server is None:
        raise FileNotFoundError(f"Сервер '{name}' не найден.")
        click.secho(f"Группа \"{name}\" не найдена!", fg="red")
        sys.exit(1)
    print(server.tcp_port)
    server.tcp_port = tcp_port
    session.commit()
    print(name, tcp_port)