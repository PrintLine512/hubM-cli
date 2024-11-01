import logging
import sys

# Декоратор для централизованной обработки ошибок и логирования
logger = logging.getLogger(__name__)

# Декоратор для централизованной обработки ошибок и логирования
def handle_errors(log_level=logging.ERROR):
    def decorator(f):
        def wrapper(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except Exception as e:
                logger.log(log_level, f"Ошибка в {f.__name__}: {str(e)}", exc_info=True)
                sys.exit(1)
        return wrapper
    return decorator

from .group_commands import group_cli
from .user_commands import user_cli
from .usb_commands import usb_cli
from .config_commands import config_cli

__all__ = ['group_cli', 'user_cli', 'config_cli', 'usb_cli']
