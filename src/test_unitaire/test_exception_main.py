import unittest
from unittest.mock import patch
from io import StringIO
import main
from test_manager_log import test_management_logging

def init():
    
    # Initialisation de la gestion des logs
    logger = test_management_logging()
    logger.info("Starting the application")
    return logger

class TestMainException(unittest.TestCase):
       
    logger = init()
    logger.info("The exception launch")

    def __init__(self, logger):
        self.logger = logger

    @patch('sys.stdout', new_callable=StringIO)
    def test_exception_handling(self, mock_stdout):
        with self.assertRaises(SystemExit) as cm:
            # Appelez la fonction main() et simulez une exception
            with patch('asyncio.run', side_effect=Exception("Test Exception")):
                main.main()
        
        # Vérifiez que le message d'erreur est correctement affiché dans les logs
        log_output = mock_stdout.getvalue()
        self.logger.debug("Exception caught:" + log_output)
        self.logger.debug("Test Exception" + log_output)
    
    logger.info("End exception launch")

if __name__ == '__main__':
    unittest.main()
