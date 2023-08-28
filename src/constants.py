import enum

# Folder projet interphone
FOLDER_VISIA_SCAN = "VisiaScan/"

# Information des trace d'erreur
ERROR_TRACE_FILE_PATH = FOLDER_VISIA_SCAN + 'Error.trace'
ERROR_PREVIOUS_TRACE_FILE_PATH = FOLDER_VISIA_SCAN + 'Error.previous.trace'

# Information des logs

LOG_TEST_FILE_PATH = FOLDER_VISIA_SCAN +"src/test_front_app.log"
LOG_FILE_PATH = FOLDER_VISIA_SCAN + "src/front_app.log"
MAX_BYTES = 1024*1024
BACKUP_COUNT = 3

# Noms de fichiers QML correspondant à chaque étape
PICTURE_WINDOW_QML = FOLDER_VISIA_SCAN + "qml/Picture_window.qml"
LUNCH_WINDOW_QML = FOLDER_VISIA_SCAN + "qml/lunch_window.qml"
MAIN_WINDOW_QML = FOLDER_VISIA_SCAN + "qml/mainWindow.qml"

class LogLevel(enum.Enum):
    INFO = "INFO"
    DEBUG = "DEBUG"
    ERROR = "ERROR"

class Time_Show_Window(enum.Enum):
    Time_Show_W1 = 0
    Time_Show_W2 = 0.5
    Time_Show_W3 = 7

# Niveau de journalisation par défaut
DEFAULT_LOG_LEVEL = LogLevel.DEBUG  # Remplacez "DEBUG" par le niveau de votre choix
DEFAULT_LOG_TEST_LEVEL = LogLevel.ERROR  