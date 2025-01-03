import configparser
# from . import handle_work
import logging
from pathlib import Path

import click

logger = logging.getLogger(__name__)


@click.group(name="config")
@click.pass_context
def config_cli(ctx):
    """Группа команд для настройки."""
    ctx.ensure_object(dict)  # Инициализация контекста как словаря


#@handle_work
@config_cli.command()
@click.option('--path', type=click.Path(), default='/etc/hubm', show_default=True,
              help="Директория hubM.", prompt=("Введите путь к директории"))
@click.option('--driver', default='postgresql', show_default=True, help="Драйвер для подключения к базе данных.", prompt = ("Введите driver"))
@click.option('--user', default='psql_user', show_default=True, help="Пользователь для подключения к базе данных.", prompt = ("Введите пользователя"))
@click.option('--password', default='irRaWUjZQ2bo9pwS7qA7', show_default=True, help="Пароль для подключения к базе данных.", prompt = ("Введите пароль"))
@click.option('--address', default='localhost', show_default=True, help="Адрес для подключения к базе данных.", prompt = ("Введите адрес"))
@click.option('--port', default='5432', type=click.IntRange(20,65535), show_default=True, help="TCP-порт для подключения к базе данных.", prompt = ("Введите порт"))
@click.option('--db-name', default='usbhub_db', show_default=True, help="Название базы данных для подключения к базе данных.", prompt = ("Введите название базы данных"))
@click.pass_context
def setup(ctx, path, driver, user, password, address, port, db_name):
    """Первичная настройка"""
    base_path = Path(path)
    config = configparser.ConfigParser()
    dirs_to_create = ['groups', 'logs']
    for dir_name in dirs_to_create:
        dir_path = base_path / dir_name
        dir_path.mkdir(parents=True, exist_ok=True)
        if ctx.obj['DEBUG']:
            click.secho(f'Папка {dir_path} успешно создана.', fg='green')

    config[ 'DEFAULT' ] = {
        'db_url': f'{driver}://{user}:{password}@{address}:{port}/{db_name}'
    }

    if ctx.obj[ 'DEBUG' ]:
        click.secho(f"Сгенерирован файл конфигурации:", fg='green')
#        for section in config.sections():
#            click.secho(f"[{section}]", fg='green')
#            for key, value in config.items(section):
#                click.secho(f"{key}: {value}", fg='green')
#            # Если у вас нет других секций, выводите значения из DEFAULT
        click.secho("[DEFAULT]", fg="yellow")
        for key, value in config[ 'DEFAULT' ].items():
            click.secho(f"{key} = {value}", fg='yellow')

    config_path = base_path / "config.ini"
    with open(config_path, 'w') as configfile:
        config.write(configfile)
    if ctx.obj[ 'DEBUG' ]:
        click.secho(f"Конфигурационный файл '{config_path}' успешно создан!", fg='green')
