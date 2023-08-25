import unittest
from unittest.mock import Mock, patch
import com_micro  # Importez ici le module que vous testez

class TestComMicro(unittest.TestCase):

    @patch('com_micro.check_microphone_presence', return_value=True)
    def test_check_microphone_presence_true(self, mock_presence):
        result = com_micro.check_microphone_presence()
        self.assertTrue(result)

    @patch('com_micro.check_microphone_presence', return_value=False)
    def test_check_microphone_presence_false(self, mock_presence):
        result = com_micro.check_microphone_presence()
        self.assertFalse(result)

    @patch('com_micro.start_microphone', return_value=True)
    def test_start_microphone_true(self, mock_start):
        result = com_micro.start_microphone()
        self.assertTrue(result)

    @patch('com_micro.start_microphone', return_value=False)
    def test_start_microphone_false(self, mock_start):
        result = com_micro.start_microphone()
        self.assertFalse(result)

    def test_record_audio_success(self):
        duration = 10
        with patch('com_micro.record_audio', return_value="recorded_audio.wav"):
            result = com_micro.record_audio(duration)
            self.assertEqual(result, "recorded_audio.wav")

    def test_record_audio_failure(self):
        duration = 10
        with patch('com_micro.record_audio', return_value=None):
            result = com_micro.record_audio(duration)
            self.assertIsNone(result)

    @patch('com_micro.stop_microphone', return_value=True)
    def test_stop_microphone_true(self, mock_stop):
        result = com_micro.stop_microphone()
        self.assertTrue(result)

    @patch('com_micro.stop_microphone', return_value=False)
    def test_stop_microphone_false(self, mock_stop):
        result = com_micro.stop_microphone()
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
