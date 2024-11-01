import click
import logging
import sys
import os
from pathlib import Path


# Настройка логгера для удобного логирования
def setup_logging(log_level=logging.INFO):
    logger = logging.getLogger(__name__)
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(log_level)
    return logger


logger = setup_logging()


# Опции глобальной настройки (например, уровень логирования)
@click.group()
@click.option('--debug', is_flag=True, help="Включить режим отладки.")
@click.pass_context
def cli(ctx, debug):
    """
    Основная точка входа для CLI.
    """
    ctx.ensure_object(dict)
    if debug:
        logger.setLevel(logging.DEBUG)
        logger.debug("Режим отладки включен")

    # Опционально: можно добавлять переменные окружения или настройки
    # в контекст, чтобы иметь к ним доступ из подкоманд
    ctx.obj[ 'DEBUG' ] = debug


@cli.command()
@click.argument('filename', type=click.Path(exists=True))
@click.option('--output', '-o', type=click.Path(), default='output.txt', help="Файл для вывода.")
@click.option('--verbose', '-v', is_flag=True, help="Подробный вывод.")
def process(filename, output, verbose):
    """
    Команда для обработки файла FILENAME.
    """
    if verbose:
        click.echo(f"Обработка файла: {filename}")

    try:
        # Пример обработки файла
        with open(filename, 'r') as f:
            data = f.read()

        # Сохранение результата
        with open(output, 'w') as f:
            f.write(data)

        click.echo(f"Результат сохранен в {output}")

    except Exception as e:
        logger.error(f"Ошибка обработки файла: {e}")
        sys.exit(1)


@cli.command()
@click.option('--name', prompt='Ваше имя', help="Имя пользователя.")
@click.option('--age', prompt='Ваш возраст', help="Возраст пользователя.", type=int)
def greet(name, age):
    """
    Приветственная команда, выводящая приветствие для пользователя.
    """
    if age < 18:
        click.echo(f"Привет, {name}! Ты молод!")
    else:
        click.echo(f"Привет, {name}! Добро пожаловать!")


@cli.command()
def setup():
    """
    Команда для первоначальной настройки.
    """
    click.echo("Настройка завершена.")


# Основной запуск CLI
def main():
    cli(obj={})


if __name__ == '__main__':
    main()
