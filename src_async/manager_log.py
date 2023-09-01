import logging
import constants
from threading import Lock
from logging.handlers import RotatingFileHandler
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

        # Initialisation d'un verrou pour le fichier de log
        self.log_lock = Lock()

    def _acquire_lock(self):
        """
        Acquérir le verrou du fichier de log.
        """
        self.log_lock.acquire()

    def _release_lock(self):
        """
        Libérer le verrou du fichier de log.
        """
        self.log_lock.release()

    def info(self, message):
        """
        Enregistrer un message d'information dans les logs.

        Args:
            message (str): Le message à enregistrer.
        """
        self._acquire_lock()
        try:
            self.logger.info(message)
        finally:
            self._release_lock()


    def error(self, message):
        """
        Enregistrer un message d'erreur dans les logs.

        Args:
            message (str): Le message d'erreur à enregistrer.
        """
        self._acquire_lock()
        try:
            self.logger.error(message)
        finally:
            self._release_lock()

    def debug(self, message):
        """
        Enregistrer un message de débogage dans les logs.

        Args:
            message (str): Le message de débogage à enregistrer.
        """
        self._acquire_lock()
        try:
            self.logger.debug(message)
        finally:
            self._release_lock()

def management_logging():
    """
    Initialiser le gestionnaire de logs.

    Returns:
        LogManager: Instance du gestionnaire de logs.
    """
    return LogManager()
