import unittest
from unittest.mock import Mock, patch
import com_soundspeaker  # Importez ici le module que vous testez

class TestComSoundSpeaker(unittest.TestCase):

    @patch('com_soundspeaker.check_speaker_presence', return_value=True)
    def test_check_speaker_presence_true(self, mock_presence):
        result = com_soundspeaker.check_speaker_presence()
        self.assertTrue(result)

    @patch('com_soundspeaker.check_speaker_presence', return_value=False)
    def test_check_speaker_presence_false(self, mock_presence):
        result = com_soundspeaker.check_speaker_presence()
        self.assertFalse(result)

    @patch('com_soundspeaker.start_speaker', return_value=True)
    def test_start_speaker_true(self, mock_start):
        result = com_soundspeaker.start_speaker()
        self.assertTrue(result)

    @patch('com_soundspeaker.start_speaker', return_value=False)
    def test_start_speaker_false(self, mock_start):
        result = com_soundspeaker.start_speaker()
        self.assertFalse(result)

    def test_play_audio_success(self):
        audio_file_path = "audio_file.wav"  # Exemple de chemin de fichier (à adapter)
        with patch('com_soundspeaker.play_audio', return_value=True):
            result = com_soundspeaker.play_audio(audio_file_path)
            self.assertTrue(result)

    def test_play_audio_failure(self):
        audio_file_path = "audio_file.wav"  # Exemple de chemin de fichier (à adapter)
        with patch('com_soundspeaker.play_audio', return_value=False):
            result = com_soundspeaker.play_audio(audio_file_path)
            self.assertFalse(result)

    @patch('com_soundspeaker.stop_speaker', return_value=True)
    def test_stop_speaker_true(self, mock_stop):
        result = com_soundspeaker.stop_speaker()
        self.assertTrue(result)

    @patch('com_soundspeaker.stop_speaker', return_value=False)
    def test_stop_speaker_false(self, mock_stop):
        result = com_soundspeaker.stop_speaker()
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
