import asyncio
import sys
from PyQt5.QtWidgets import QApplication
from frontend import frontEnd_process
from backend import backEndExt_process, backEndInt_process
from manager_log import management_logging
from manager_error import call_exception

def init():
    # Initialisation de la gestion des logs
    logger = management_logging()
    logger.info("Starting the application")
    return logger

async def run_process():
    """
    Fonction pour exécuter les tâches asynchrones.
    """
    logger = init()

    try:
        # Création des tâches asynchrones
        tasks = [
            frontEnd_process(logger),
            backEndExt_process(logger),
            backEndInt_process(logger)
        ]

        # Lancement des tâches en parallèle
        logger.info("The task launch")
        await asyncio.gather(*tasks)

    except Exception as e:
        call_exception(e, logger)
 

async def main():
    """
    Fonction principale pour lancer l'application Qt et exécuter les tâches.
    """
    # Initialisation de l'application Qt
    app = QApplication(sys.argv)
    await run_process()
    sys.exit(app.exec_())

if __name__ == "__main__":
    asyncio.run(main())
