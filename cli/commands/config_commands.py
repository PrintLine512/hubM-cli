import click
from . import handle_errors
import logging
import sys
from pathlib import Path
import subprocess

logger = logging.getLogger(__name__)


@click.group(name="config")
def config_cli():
    """Группа команд для настройки."""
    pass


@handle_errors()
@config_cli.command()
#@click.option('--config-path', type=click.Path(), default='~/.mycli/config.json', show_default=True,
#              help="Путь к файлу конфигурации.")
def setup():
    try:
        subprocess.run([ "HUB-CORE", "-b", "-c", "/usr/local/etc/virtualhere/groups/Test.ini"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        sys.exit()
    except Exception as e:
        sys.exit(1)


def setup2(config_path):
    """Первоначальная настройка CLI. Создает конфигурационный файл."""
    config_path = Path(config_path).expanduser()

    if not config_path.parent.exists():
        config_path.parent.mkdir(parents=True)

    try:
        with open(config_path, 'w') as f:
            f.write('{"configured": true}')
        click.secho(f"Конфигурация завершена. Файл создан в {config_path}", fg="green")
        logger.info(f"Конфигурация завершена: {config_path}")

    except IOError as e:
        logger.error(f"Ошибка записи конфигурации: {str(e)}")
        click.secho(f"Ошибка записи конфигурации: {str(e)}", fg="red")
        sys.exit(1)
