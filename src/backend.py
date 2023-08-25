import asyncio
from manager_log import LogManager

class BackEnd:
    def __init__(self, logger):
        self.logger = logger

    async def handle_external_events(self):
        while True:
            # Placeholder for handling external events
            self.logger.debug("B - External event handled")
            await asyncio.sleep(1)

    async def handle_internal_events(self):
        while True:
            # Placeholder for handling internal events
            self.logger.debug("B - Internal event handled")
            await asyncio.sleep(1)

async def backEndExt_process(logger):
    backend = BackEnd(logger)
    logger.info("B - Starting external backend process")
    await backend.handle_external_events()

async def backEndInt_process(logger):
    backend = BackEnd(logger)
    logger.info("B - Starting internal backend process")
    await backend.handle_internal_events()
