from loguru import logger as logutil
from datetime import datetime

class Logger:

    def __init__(self, log_file=''):
        self.logger = logutil
        if log_file:
            self.logger.add(log_file, encoding="utf-8")


    def info(self, message, *args, **kwargs):
        """
            info
        """
        self.logger.info(message, *args, **kwargs)

    def debug(self, message, *args, **kwargs):
        """
            debug
        """
        self.logger.debug(message, *args, **kwargs)

    def success(self, message, *args, **kwargs):
        """
            success
        """
        self.logger.success(message, *args, **kwargs)

    def error(self, message, *args, **kwargs):
        """
            error
        """
        self.logger.error(message, *args, **kwargs)

    def critical(self, message, *args, **kwargs):
        """
            critical
        """
        self.logger.critical(message, *args, **kwargs)

    def warning(self, message, *args, **kwargs):
        """
            warning
        """
        self.logger.warning(message, *args, **kwargs)


log_file = f'log/{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}-log.log'
logger = Logger(log_file=log_file )