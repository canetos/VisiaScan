import sys
import threading
from PyQt5.QtWidgets import QApplication
from frontend import FrontEnd
from backend import Backend
from manager_log import management_logging
from manager_error import call_exception
from constants import *
import manager_reset_file

def init():
    # Initialize log management
    logger = management_logging()
    logger.info("Starting the application")
    
    # Reset log and trace files
    manager_reset_file.init_reset_file(logger)
    
    return logger

def run_processes(logger):
    """
    Function to run tasks in parallel using threads.
    """
    try:
        # Create instances of classes
        main_app = FrontEnd(logger)
        backend = Backend()

        # Create threads
        frontend_thread = threading.Thread(target=main_app.handle_ui_events)
        backend_thread = threading.Thread(target=backend.process)

        # Start threads
        frontend_thread.start()
        backend_thread.start()

        # Wait for threads to finish
        frontend_thread.join()
        backend_thread.join()

    except Exception as e:
        call_exception(e, logger)

def main():
    """
    Main function to launch the Qt application and run tasks.
    """
    # Initialize the Qt application
    app = QApplication(sys.argv)
    
    logger = init()
    run_processes(logger)
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
