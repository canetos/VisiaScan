import unittest
from unittest.mock import Mock, patch
import authentification  # Importez ici le module que vous testez

class TestAuthentification(unittest.TestCase):

    @patch('authentification.auth.get_user')
    def test_new_authent(self, mock_get_user):
        # Mock necessary functions and methods
        mock_user = Mock()
        mock_user.uid = 'QTDa6sdj98YvBVQEYoQBmYmgmdD2'
        mock_get_user.return_value = mock_user
        
        app_mock = Mock()
        user_data = authentification.new_authent(app_mock)
        
        mock_get_user.assert_called_once_with('QTDa6sdj98YvBVQEYoQBmYmgmdD2')
        self.assertEqual(user_data.uid, 'QTDa6sdj98YvBVQEYoQBmYmgmdD2')

    @patch('authentification.auth.create_custom_token')
    def test_create_token(self, mock_create_custom_token):
        # Mock necessary functions and methods
        mock_create_custom_token.return_value = 'dummy_token'
        
        app_mock = Mock()
        token = authentification.create_tokken(app_mock, 'QTDa6sdj98YvBVQEYoQBmYmgmdD2')
        
        mock_create_custom_token.assert_called_once_with(
            'QTDa6sdj98YvBVQEYoQBmYmgmdD2', {'premiumAccount': True})
        self.assertEqual(token, 'dummy_token')

if __name__ == '__main__':
    unittest.main()
