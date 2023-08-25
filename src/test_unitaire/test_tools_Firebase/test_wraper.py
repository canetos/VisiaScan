import unittest
from unittest.mock import Mock, patch
import wraper  # Importez ici le module que vous testez

class TestWrapper(unittest.TestCase):

    @patch('wraper.connexion')
    def test_create_connexion(self, mock_connexion):
        # Mock necessary objects and methods
        mock_json_path = 'path/to/json/file.json'
        mock_connexion.create_connexion.return_value = ('app_mock', 'db_mock')
        
        result = wraper.create_connexion(mock_json_path)
        
        mock_connexion.create_connexion.assert_called_once_with(mock_json_path)
        self.assertEqual(result, ('app_mock', 'db_mock'))

    @patch('wraper.function')
    def test_del_base(self, mock_function):
        # Mock necessary objects and methods
        mock_db = Mock()
        collection = 'my_collection'
        document = 'my_document'
        mock_function.del_base.return_value = 'result_mock'
        
        result = wraper.del_base(mock_db, collection, document)
        
        mock_function.del_base.assert_called_once_with(mock_db, collection, document)
        self.assertEqual(result, 'result_mock')

    @patch('wraper.function')
    def test_print_collection(self, mock_function):
        # Mock necessary objects and methods
        mock_db = Mock()
        collection = 'my_collection'
        mock_function.print_collection.return_value = 'result_mock'
        
        result = wraper.print_collection(mock_db, collection)
        
        mock_function.print_collection.assert_called_once_with(mock_db, collection)
        self.assertEqual(result, 'result_mock')

    @patch('wraper.function')
    def test_get_data(self, mock_function):
        # Mock necessary objects and methods
        mock_db = Mock()
        collection = 'my_collection'
        mock_function.get_data.return_value = 'result_mock'
        
        result = wraper.get_data(mock_db, collection)
        
        mock_function.get_data.assert_called_once_with(mock_db, collection)
        self.assertEqual(result, 'result_mock')

    @patch('wraper.function')
    def test_add_value(self, mock_function):
        # Mock necessary objects and methods
        mock_db = Mock()
        collection = 'my_collection'
        document = 'my_document'
        key = 'my_key'
        kwargs = {'field2': 'value2'}
        mock_function.add_value.return_value = 'result_mock'
        
        result = wraper.add_value(mock_db, collection, document, key, **kwargs)
        
        mock_function.add_value.assert_called_once_with(mock_db, collection, document, key, **kwargs)
        self.assertEqual(result, 'result_mock')

if __name__ == '__main__':
    unittest.main()
