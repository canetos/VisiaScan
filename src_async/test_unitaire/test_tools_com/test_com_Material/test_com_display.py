import unittest
from unittest.mock import Mock, patch
import com_display  # Importez ici le module que vous testez

class TestComDisplay(unittest.TestCase):

    @patch('com_display.check_display_presence', return_value=True)
    def test_check_display_presence_true(self, mock_presence):
        result = com_display.check_display_presence()
        self.assertTrue(result)

    @patch('com_display.check_display_presence', return_value=False)
    def test_check_display_presence_false(self, mock_presence):
        result = com_display.check_display_presence()
        self.assertFalse(result)

    @patch('com_display.start_display', return_value=True)
    def test_start_display_true(self, mock_start):
        result = com_display.start_display()
        self.assertTrue(result)

    @patch('com_display.start_display', return_value=False)
    def test_start_display_false(self, mock_start):
        result = com_display.start_display()
        self.assertFalse(result)

    @patch('com_display.show_text', return_value=True)
    def test_show_text_true(self, mock_show):
        result = com_display.show_text("Test Text")
        self.assertTrue(result)

    @patch('com_display.show_text', return_value=False)
    def test_show_text_false(self, mock_show):
        result = com_display.show_text("Test Text")
        self.assertFalse(result)

    @patch('com_display.clear_display', return_value=True)
    def test_clear_display_true(self, mock_clear):
        result = com_display.clear_display()
        self.assertTrue(result)

    @patch('com_display.clear_display', return_value=False)
    def test_clear_display_false(self, mock_clear):
        result = com_display.clear_display()
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
