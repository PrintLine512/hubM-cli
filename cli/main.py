import click
#from commands.user_commands import user_cli
#from commands.config_commands import config_cli
from commands import config_cli, user_cli, usb_cli, group_cli
import logging
import sys


# Настройка логгера для CLI
def setup_logging(log_level=logging.INFO, log_file=None):
    logger = logging.getLogger(__name__)
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    logger.setLevel(log_level)
    return logger


logger = setup_logging()


@click.group()
@click.option('--debug', is_flag=True, help="Включить режим отладки.")
@click.option('--log-file', type=click.Path(), help="Файл для сохранения логов.")
@click.pass_context
def cli(ctx, debug, log_file):
    """
    Основная точка входа CLI. Используйте --help для справки.
    """
    ctx.ensure_object(dict)
    if debug:
        logger.setLevel(logging.DEBUG)
        logger.debug("Режим отладки включен")

    if log_file:
        setup_logging(log_level=logging.DEBUG if debug else logging.INFO, log_file=log_file)


# Добавление команд
cli.add_command(group_cli)
cli.add_command(usb_cli)
cli.add_command(user_cli)
cli.add_command(config_cli)

# Запуск CLI
def main():
    cli(obj={})

if __name__ == '__main__':
    main()
