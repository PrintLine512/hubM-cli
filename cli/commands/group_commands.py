from importlib import import_module
import sqlalchemy
import click
from sqlalchemy.orm import sessionmaker
from sqlalchemy.util import assert_arg_type

from . import handle_errors
from templates.models import server_model
from config import db_url

import logging
import subprocess, sys

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
    try:
        subprocess.run([ "HUB-CORE", "-b", "-c", "/usr/local/etc/virtualhere/groups/Test.ini"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        logger.info(f"Приветствие отправлено для пользователя: {name}, возраст: ")
        sys.exit()
    except Exception as e:
        logger.critical(e)
        sys.exit(1)


@handle_errors()
@group_cli.command()
@click.option('--name', help="Название группы.")
def conf(name):

    engine = sqlalchemy.create_engine(db_url, pool_size=20, max_overflow=0, pool_recycle=10, pool_timeout=10)
    Session = sessionmaker(bind=engine)

    session = Session()
    #server = session.query(server_model).filter_by(name=name).first()
    #print(server.name)
