# Objectif de faire appel au projet de face_roco.py lors de l'appuis du bouton sur l'interface

import face_roco  # Importez ici le module que vous souhaitez appeler
import logging

logger = logging.getLogger(__name__)

def call_IA_on_button_press():
    """
    Appelle le projet de reconnaissance faciale lorsque le bouton est pressé.

    :return: True si l'appel à l'IA a réussi, False sinon.
    :rtype: bool
    """
    try:
        # Appel au projet de reconnaissance faciale
        result = face_roco.recognize_faces()  # Remplacez cette ligne par l'appel réel à votre projet
        if result:
            logger.info("Face recognition project called successfully.")
        else:
            logger.error("Failed to call face recognition project.")
        return result
    except Exception:
        logger.error("Failed to call face recognition project.")
        return False
