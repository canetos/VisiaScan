import asyncio
import unittest
from unittest.mock import Mock, patch
from PyQt5.QtWidgets import QApplication
from main import init, run_process, main

class TestMain(unittest.TestCase):

    def setUp(self):
        self.app = QApplication([])  # Create a QApplication for testing

    def test_init(self):
        logger = init()
        self.assertIsNotNone(logger)  # Check if logger is initialized

    @patch('asyncio.gather')
    @patch('asyncio.run')
    @patch('asyncio.sleep')
    async def test_run_process_successful(self, mock_sleep, mock_run, mock_gather):
        # Mock the necessary functions and classes
        logger_mock = Mock()
        app_mock = Mock()
        app_mock.exec_.return_value = 0
        app_mock.exit.return_value = None
        app_mock.exec_.side_effect = asyncio.CancelledError  # To exit the event loop

        # Configure mocks
        mock_sleep.side_effect = [None, None]  # For asyncio.sleep calls
        mock_gather.return_value = None

        with patch('main.QApplication', return_value=app_mock):
            with patch('main.init', return_value=logger_mock):
                await run_process()

        # Assertions
        mock_gather.assert_called_once()  # Check if asyncio.gather is called
        mock_sleep.assert_called()  # Check if asyncio.sleep is called

    @patch('asyncio.run')
    @patch('main.run_process')
    async def test_main(self, mock_run_process, mock_run):
        # Configure mocks
        mock_run_process.return_value = None

        # Run the main function
        await main()

        # Assertions
        mock_run_process.assert_called_once()  # Check if run_process is called
        mock_run.assert_called_once()  # Check if asyncio.run is called

if __name__ == '__main__':
    unittest.main()
