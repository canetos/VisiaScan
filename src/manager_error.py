import constants

def call_exception(e, logger):
 # Condition pour la gestion spécifique d'une exception
        if isinstance(e, KeyboardInterrupt):
            logger.info("Application terminated by user")
        else:
            call_exception_msg(e, logger)

def call_exception_msg(e, logger):
    error_message = f"An error occurred: {str(e)}"
    logger.error(error_message)
    log_error(error_message)

def log_error(message):
    """
    Enregistrer le message d'erreur dans le fichier Error.trace.
    
    Args:
        message (str): Le message d'erreur à enregistrer.
    """
    with open(constants.ERROR_TRACE_FILE_PATH, 'a') as error_file:
        error_file.write(message + '\n')