import unittest
from unittest.mock import Mock, patch
import com_app_mobile  # Importez ici le module que vous testez

class TestComAppMobile(unittest.TestCase):

    @patch('socket.socket')
    def test_connect_to_mobile_app_success(self, mock_socket):
        mock_socket.return_value.connect.return_value = None
        result = com_app_mobile.connect_to_mobile_app("192.168.1.1", 8080)
        self.assertIsNone(result)

    @patch('socket.socket')
    def test_send_command_to_mobile_app_success(self, mock_socket):
        mock_socket.return_value.sendall.return_value = None
        mobile_socket = mock_socket.return_value
        result = com_app_mobile.send_command_to_mobile_app(mobile_socket, "test_command")
        self.assertTrue(result)

    @patch('socket.socket')
    def test_receive_response_from_mobile_app_success(self, mock_socket):
        mock_socket.return_value.recv.return_value.decode.return_value = "test_response"
        mobile_socket = mock_socket.return_value
        result = com_app_mobile.receive_response_from_mobile_app(mobile_socket)
        self.assertEqual(result, "test_response")

    @patch('socket.socket')
    def test_close_mobile_connection_success(self, mock_socket):
        mock_socket.return_value.close.return_value = None
        mobile_socket = mock_socket.return_value
        com_app_mobile.close_mobile_connection(mobile_socket)

if __name__ == '__main__':
    unittest.main()
