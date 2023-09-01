# reset_file_manager.py
import os
import constants

def init_reset_file(self):
    # Initialisation de la trace.
    _reset_error_trace()
    self.logger.info('File log reset')
    _reset_log_file()
    self.logger.info('File trace reset')

def _reset_file(log_file_path):
    if os.path.exists(log_file_path):
        os.remove(log_file_path)
    open(log_file_path, 'a').close()

def _reset_log_file():
    """
    Réinitialise le fichier de logs en le supprimant et en recréant un nouveau fichier vide.
    """
    _reset_file(log_file_path = constants.LOG_FILE_PATH)

def _reset_error_trace():
    """
    Réinitialise le fichier de trace d'erreurs en le renommant comme Error.previous.trace.
    """
    error_trace_path = constants.ERROR_TRACE_FILE_PATH
    if os.path.exists(error_trace_path):
        os.remove(error_trace_path)
    open(error_trace_path, 'a').close()