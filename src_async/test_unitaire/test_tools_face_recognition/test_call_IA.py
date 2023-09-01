import unittest
from unittest.mock import Mock, patch
import call_IA  # Importez ici le module que vous testez

class TestCallIA(unittest.TestCase):

    @patch('call_IA.face_roco.recognize_faces', return_value=True)
    def test_call_IA_on_button_press_success(self, mock_recognize):
        result = call_IA.call_IA_on_button_press()
        self.assertTrue(result)

    @patch('call_IA.face_roco.recognize_faces', return_value=False)
    def test_call_IA_on_button_press_failure(self, mock_recognize):
        result = call_IA.call_IA_on_button_press()
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
