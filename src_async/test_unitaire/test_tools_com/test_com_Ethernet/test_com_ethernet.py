import unittest
from unittest.mock import Mock, patch
import com_ethernet  # Importez ici le module que vous testez

class TestComEthernet(unittest.TestCase):

    @patch('socket.socket')
    def test_is_ethernet_available_true(self, mock_socket):
        result = com_ethernet.is_ethernet_available()
        self.assertTrue(result)

    @patch('socket.socket', side_effect=OSError)
    def test_is_ethernet_available_false(self, mock_socket):
        result = com_ethernet.is_ethernet_available()
        self.assertFalse(result)

    @patch('socket.create_connection')
    def test_is_internet_reachable_true(self, mock_create_connection):
        result = com_ethernet.is_internet_reachable()
        self.assertTrue(result)

    @patch('socket.create_connection', side_effect=OSError)
    def test_is_internet_reachable_false(self, mock_create_connection):
        result = com_ethernet.is_internet_reachable()
        self.assertFalse(result)

    @patch('com_ethernet.is_ethernet_available', return_value=True)
    @patch('com_ethernet.is_internet_reachable', return_value=True)
    def test_check_ethernet_connection_success(self, mock_internet, mock_ethernet):
        result = com_ethernet.check_ethernet_connection()
        self.assertEqual(result, {"ethernet_available": True, "internet_reachable": True})

    @patch('com_ethernet.is_ethernet_available', return_value=False)
    @patch('com_ethernet.is_internet_reachable', return_value=False)
    def test_check_ethernet_connection_failure(self, mock_internet, mock_ethernet):
        result = com_ethernet.check_ethernet_connection()
        self.assertEqual(result, {"ethernet_available": False, "internet_reachable": False})

if __name__ == '__main__':
    unittest.main()
