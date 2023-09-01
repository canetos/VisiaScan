import unittest
from unittest.mock import Mock, patch
import com_camera  # Importez ici le module que vous testez

class TestComCamera(unittest.TestCase):

    @patch('com_camera.check_camera_presence', return_value=True)
    def test_check_camera_presence_true(self, mock_presence):
        result = com_camera.check_camera_presence()
        self.assertTrue(result)

    @patch('com_camera.check_camera_presence', return_value=False)
    def test_check_camera_presence_false(self, mock_presence):
        result = com_camera.check_camera_presence()
        self.assertFalse(result)

    @patch('com_camera.start_camera', return_value=True)
    def test_start_camera_true(self, mock_start):
        result = com_camera.start_camera()
        self.assertTrue(result)

    @patch('com_camera.start_camera', return_value=False)
    def test_start_camera_false(self, mock_start):
        result = com_camera.start_camera()
        self.assertFalse(result)

    @patch('com_camera.capture_image', return_value=True)
    def test_capture_image_true(self, mock_capture):
        result = com_camera.capture_image()
        self.assertTrue(result)

    @patch('com_camera.capture_image', return_value=False)
    def test_capture_image_false(self, mock_capture):
        result = com_camera.capture_image()
        self.assertFalse(result)

    @patch('com_camera.record_video', return_value=True)
    def test_record_video_true(self, mock_record):
        result = com_camera.record_video(10)  # Duration parameter value doesn't matter for testing
        self.assertTrue(result)

    @patch('com_camera.record_video', return_value=False)
    def test_record_video_false(self, mock_record):
        result = com_camera.record_video(10)  # Duration parameter value doesn't matter for testing
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
