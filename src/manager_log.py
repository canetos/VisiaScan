import logging
from logging.handlers import RotatingFileHandler
import constants
from manager_reset_file import init_reset_file

class LogManager:
    """
    Classe pour la gestion des logs :
    """

    def __init__(self):
        """
        Initialisation du gestionnaire de logs et des traces d'erreur.
        """
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(constants.DEFAULT_LOG_LEVEL.value)

        init_reset_file(self)

        # Configuration du gestionnaire de fichiers de logs
        log_file_path = constants.LOG_FILE_PATH
        max_bytes = constants.MAX_BYTES
        backup_count = constants.BACKUP_COUNT
        contents_formatter = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

        handler = RotatingFileHandler(log_file_path, maxBytes=max_bytes, backupCount=backup_count)
        formatter = logging.Formatter(contents_formatter)
        handler.setFormatter(formatter)

        self.logger.addHandler(handler)

    def info(self, message):
        """
        Enregistrer un message d'information dans les logs.

        Args:
            message (str): Le message à enregistrer.
        """
        self.logger.info(message)

    def error(self, message):
        """
        Enregistrer un message d'erreur dans les logs.

        Args:
            message (str): Le message d'erreur à enregistrer.
        """
        self.logger.error(message)

    def debug(self, message):
        """
        Enregistrer un message de débogage dans les logs.

        Args:
            message (str): Le message de débogage à enregistrer.
        """
        self.logger.debug(message)

def management_logging():
    """
    Initialiser le gestionnaire de logs.

    Returns:
        LogManager: Instance du gestionnaire de logs.
    """
    return LogManager()
