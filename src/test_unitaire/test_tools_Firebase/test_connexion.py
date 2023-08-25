import unittest
from unittest.mock import Mock, patch
import connexion  # Importez ici le module que vous testez

class TestConnexion(unittest.TestCase):

    @patch('connexion.firebase_admin.initialize_app')
    @patch('connexion.firestore.client')
    @patch('connexion.credentials.Certificate')
    def test_create_connexion_success(self, mock_certificate, mock_firestore_client, mock_initialize_app):
        # Mock necessary functions and methods
        mock_cred = Mock()
        mock_certificate.return_value = mock_cred
        
        app_mock = Mock()
        db_mock = Mock()
        mock_initialize_app.return_value = app_mock
        mock_firestore_client.return_value = db_mock
        
        json_path = 'dummy.json'
        app, db = connexion.create_connexion(json_path)
        
        mock_certificate.assert_called_once_with(json_path)
        mock_initialize_app.assert_called_once_with(mock_cred)
        mock_firestore_client.assert_called_once()
        self.assertEqual(app, app_mock)
        self.assertEqual(db, db_mock)

    @patch('connexion.firebase_admin.initialize_app', side_effect=Exception('Failed to initialize app'))
    def test_create_connexion_failure(self, mock_initialize_app):
        json_path = 'dummy.json'
        app, db = connexion.create_connexion(json_path)
        
        mock_initialize_app.assert_called_once()
        self.assertIsNone(app)
        self.assertIsNone(db)

if __name__ == '__main__':
    unittest.main()
