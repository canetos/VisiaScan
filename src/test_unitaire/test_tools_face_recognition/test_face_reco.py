import unittest
from unittest.mock import Mock, patch
import face_reco  # Importez ici le module que vous testez

class TestFaceReco(unittest.TestCase):

    @patch('face_reco.cv2.imread')
    @patch('face_reco.dlib.get_frontal_face_detector')
    @patch('face_reco.dlib.shape_predictor')
    @patch('face_reco.cv2.imshow')
    @patch('face_reco.cv2.waitKey')
    @patch('face_reco.cv2.destroyAllWindows')
    def test_face_reco_process(self, mock_destroyAllWindows, mock_waitKey, mock_imshow,
                               mock_shape_predictor, mock_frontal_face_detector,
                               mock_imread):
        # Mock necessary functions and methods
        mock_face_detector = Mock()
        mock_shape_predictor_instance = Mock()
        mock_face = Mock()
        mock_landmarks = Mock()
        mock_landmarks.parts.return_value = [{'x': 100, 'y': 200}]
        
        mock_frontal_face_detector.return_value = mock_face_detector
        mock_shape_predictor.return_value = mock_shape_predictor_instance
        mock_face_detector.return_value = [mock_face]
        mock_imread.return_value = 'dummy_image'
        
        face_reco.face_reco_process('path/to/your/image.jpg')
        
        mock_frontal_face_detector.assert_called_once()
        mock_shape_predictor.assert_called_once()
        mock_face_detector.assert_called_once()
        mock_imread.assert_called_once_with('path/to/your/image.jpg')
        mock_imshow.assert_called_once()
        mock_waitKey.assert_called_once()
        mock_destroyAllWindows.assert_called_once()

if __name__ == '__main__':
    unittest.main()
