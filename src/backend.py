import asyncio
from manager_log import LogManager

class BackEnd:
    """
    Classe BackEnd pour gérer les processus en arrière-plan.
    """

    def __init__(self, logger):
        """
        Initialisation de la classe BackEnd.

        :param logger: Instance du gestionnaire de logs.
        :type logger: LogManager
        """
        self.logger = logger
        self.is_running = True  # Variable pour contrôler la boucle

    async def handle_external_events(self):
        """
        Gère les événements externes en arrière-plan.

        Cette méthode exécute une boucle en attendant les événements externes.

        :return: Rien.
        :rtype: None
        """
        while self.is_running:  # Utilisation de la variable pour contrôler la boucle
            # Placeholder for handling external events
            self.logger.debug("B - External event handled")
            await asyncio.sleep(1)

    async def handle_internal_events(self):
        """
        Gère les événements internes en arrière-plan.

        Cette méthode exécute une boucle en attendant les événements internes.

        :return: Rien.
        :rtype: None
        """
        while self.is_running:  # Utilisation de la variable pour contrôler la boucle
            # Placeholder for handling internal events
            self.logger.debug("B - Internal event handled")
            await asyncio.sleep(1)

    def stop(self):
        """
        Arrête la boucle de gestion des événements.

        Cette méthode met fin à la boucle en modifiant la variable is_running.

        :return: Rien.
        :rtype: None
        """
        self.is_running = False  # Mettre fin à la boucle

async def backEndExt_process(logger):
    """
    Exécute le processus de gestion des événements externes en arrière-plan.

    :param logger: Instance du gestionnaire de logs.
    :type logger: LogManager
    :return: Rien.
    :rtype: None
    """
    backend = BackEnd(logger)
    logger.info("B - Starting external backend process")
    await backend.handle_external_events()

async def backEndInt_process(logger):
    """
    Exécute le processus de gestion des événements internes en arrière-plan.

    :param logger: Instance du gestionnaire de logs.
    :type logger: LogManager
    :return: Rien.
    :rtype: None
    """
    backend = BackEnd(logger)
    logger.info("B - Starting internal backend process")
    await backend.handle_internal_events()