"""
Module com_ethernet - Fonctions de vérification de la connexion Ethernet
"""

import socket
import logging

logger = logging.getLogger(__name__)

def is_ethernet_available():
    """
    Vérifie si la connexion Ethernet est disponible.

    :return: True si la connexion est disponible, False sinon.
    :rtype: bool
    """
    try:
        # Crée un socket pour vérifier la connexion
        socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        logger.info("Ethernet connection is available.")
        return True
    except OSError:
        logger.warning("Ethernet connection is not available.")
        return False

def is_internet_reachable(host="www.google.com"):
    """
    Vérifie si Internet est accessible en utilisant un hôte de test.

    :param host: L'hôte à utiliser pour le test d'accessibilité Internet.
    :type host: str
    :return: True si Internet est accessible, False sinon.
    :rtype: bool
    """
    try:
        socket.create_connection((host, 80))
        logger.info("Internet is reachable.")
        return True
    except OSError:
        logger.warning("Internet is not reachable.")
        return False

def check_ethernet_connection():
    """
    Vérifie la connexion Ethernet et l'accessibilité à Internet.

    :return: Un dictionnaire contenant les résultats de vérification.
    :rtype: dict
    """
    results = {
        "ethernet_available": is_ethernet_available(),
        "internet_reachable": is_internet_reachable()
    }
    return results
