import unittest
from unittest.mock import Mock, patch
import com_touch_display  # Importez ici le module que vous testez

class TestComTouchDisplay(unittest.TestCase):

    @patch('com_touch_display.check_touch_display_presence', return_value=True)
    def test_check_touch_display_presence_true(self, mock_presence):
        result = com_touch_display.check_touch_display_presence()
        self.assertTrue(result)

    @patch('com_touch_display.check_touch_display_presence', return_value=False)
    def test_check_touch_display_presence_false(self, mock_presence):
        result = com_touch_display.check_touch_display_presence()
        self.assertFalse(result)

    @patch('com_touch_display.start_touch_display', return_value=True)
    def test_start_touch_display_true(self, mock_start):
        result = com_touch_display.start_touch_display()
        self.assertTrue(result)

    @patch('com_touch_display.start_touch_display', return_value=False)
    def test_start_touch_display_false(self, mock_start):
        result = com_touch_display.start_touch_display()
        self.assertFalse(result)

    @patch('com_touch_display.read_touch_input', return_value=True)
    def test_read_touch_input_success(self, mock_read):
        result = com_touch_display.read_touch_input()
        self.assertTrue(result)

    @patch('com_touch_display.read_touch_input', return_value=False)
    def test_read_touch_input_failure(self, mock_read):
        result = com_touch_display.read_touch_input()
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
