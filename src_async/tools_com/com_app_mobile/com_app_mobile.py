"""
Module com_app_mobile - Fonctions de connexion à distance à une application mobile
"""

import socket
import logging

logger = logging.getLogger(__name__)

def connect_to_mobile_app(ip_address, port):
    """
    Établit une connexion à distance avec une application mobile.

    :param ip_address: L'adresse IP de l'appareil mobile.
    :type ip_address: str
    :param port: Le numéro de port pour la connexion.
    :type port: int
    :return: Un objet de socket pour la connexion.
    :rtype: socket.socket
    """
    try:
        mobile_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mobile_socket.connect((ip_address, port))
        logger.info("Connected to the mobile app at %s:%d.", ip_address, port)
        return mobile_socket
    except OSError as e:
        logger.error("Failed to connect to the mobile app: %s", e)
        return None

def send_command_to_mobile_app(mobile_socket, command):
    """
    Envoie une commande à l'application mobile via la connexion à distance.

    :param mobile_socket: L'objet socket pour la connexion.
    :type mobile_socket: socket.socket
    :param command: La commande à envoyer.
    :type command: str
    :return: True si la commande a été envoyée avec succès, False sinon.
    :rtype: bool
    """
    try:
        mobile_socket.sendall(command.encode())
        logger.info("Command '%s' sent to the mobile app.", command)
        return True
    except OSError:
        logger.error("Failed to send command to the mobile app.")
        return False

def receive_response_from_mobile_app(mobile_socket):
    """
    Reçoit la réponse de l'application mobile via la connexion à distance.

    :param mobile_socket: L'objet socket pour la connexion.
    :type mobile_socket: socket.socket
    :return: La réponse reçue de l'application mobile.
    :rtype: str
    """
    try:
        response = mobile_socket.recv(1024).decode()
        logger.info("Received response from the mobile app: %s", response)
        return response
    except OSError:
        logger.error("Failed to receive response from the mobile app.")
        return ""

def close_mobile_connection(mobile_socket):
    """
    Ferme la connexion à distance avec l'application mobile.

    :param mobile_socket: L'objet socket pour la connexion.
    :type mobile_socket: socket.socket
    """
    try:
        mobile_socket.close()
        logger.info("Closed the connection to the mobile app.")
    except OSError:
        logger.error("Failed to close the connection to the mobile app.")
