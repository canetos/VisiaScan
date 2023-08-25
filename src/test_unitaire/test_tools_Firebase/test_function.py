import unittest
from unittest.mock import Mock, patch
import functions  # Importez ici le module que vous testez

class TestFunctions(unittest.TestCase):

    @patch('functions.firestore')
    def test_del_base(self, mock_firestore):
        # Mock necessary objects and methods
        mock_db = Mock()
        mock_doc_ref = Mock()
        mock_firestore.client.return_value = mock_db
        mock_db.collection.return_value.document.return_value = mock_doc_ref
        
        collection = 'my_collection'
        document = 'my_document'
        functions.del_base(mock_db, collection, document)
        
        mock_firestore.client.assert_called_once()
        mock_db.collection.assert_called_once_with(collection)
        mock_db.collection.return_value.document.assert_called_once_with(document)
        mock_doc_ref.set.assert_called_once_with({})

    @patch('functions.firestore')
    def test_print_collection(self, mock_firestore):
        # Mock necessary objects and methods
        mock_db = Mock()
        mock_firestore.client.return_value = mock_db
        mock_collection_ref = Mock()
        mock_db.collection.return_value = mock_collection_ref
        mock_doc1 = Mock()
        mock_doc2 = Mock()
        mock_collection_ref.stream.return_value = [mock_doc1, mock_doc2]
        mock_doc1.id = 'doc1_id'
        mock_doc1.to_dict.return_value = {'field1': 'value1'}
        mock_doc2.id = 'doc2_id'
        mock_doc2.to_dict.return_value = {'field2': 'value2'}
        
        collection = 'my_collection'
        expected_output = "doc1_id => {'field1': 'value1'}\ndoc2_id => {'field2': 'value2'}\n"
        with patch('builtins.print') as mock_print:
            functions.print_collection(mock_db, collection)
            mock_firestore.client.assert_called_once()
            mock_db.collection.assert_called_once_with(collection)
            mock_collection_ref.stream.assert_called_once()
            mock_doc1.to_dict.assert_called_once()
            mock_doc2.to_dict.assert_called_once()
            mock_print.assert_called_once_with(expected_output)

    @patch('functions.firestore')
    def test_get_data(self, mock_firestore):
        # Mock necessary objects and methods
        mock_db = Mock()
        mock_firestore.client.return_value = mock_db
        mock_collection_ref = Mock()
        mock_db.collection.return_value = mock_collection_ref
        mock_doc1 = Mock()
        mock_doc2 = Mock()
        mock_collection_ref.stream.return_value = [mock_doc1, mock_doc2]
        
        collection = 'my_collection'
        result = functions.get_data(mock_db, collection)
        
        mock_firestore.client.assert_called_once()
        mock_db.collection.assert_called_once_with(collection)
        mock_collection_ref.stream.assert_called_once()
        self.assertEqual(result, [mock_doc1, mock_doc2])

    @patch('functions.firestore')
    def test_add_value(self, mock_firestore):
        # Mock necessary objects and methods
        mock_db = Mock()
        mock_firestore.client.return_value = mock_db
        mock_collection_ref = Mock()
        mock_db.collection.return_value = mock_collection_ref
        mock_doc_ref = Mock()
        mock_db.collection.return_value.document.return_value = mock_doc_ref
        mock_stream_doc = Mock()
        mock_stream_doc.id = 'doc1_id'
        mock_stream_doc.to_dict.return_value = {'field1': 'value1'}
        mock_collection_ref.stream.return_value = [mock_stream_doc]
        
        collection = 'my_collection'
        document = 'my_document'
        key = 'my_key'
        kwargs = {'field2': 'value2'}
        functions.add_value(mock_db, collection, document, key, **kwargs)
        
        mock_firestore.client.assert_called_once()
        mock_db.collection.assert_called_once_with(collection)
        mock_db.collection.return_value.document.assert_called_once_with(document)
        mock_collection_ref.stream.assert_called_once()
        mock_stream_doc.to_dict.assert_called_once()
        mock_doc_ref.set.assert_called_once_with({'doc1_id': {'field1': 'value1', 'my_key': {'field2': 'value2'}}})

if __name__ == '__main__':
    unittest.main()
