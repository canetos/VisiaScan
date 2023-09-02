import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QLineEdit,
    QDesktopWidget, QHBoxLayout, QMessageBox, QLabel, QDialog, QFrame, QGridLayout, QCheckBox
)
from PyQt5.QtCore import Qt, QTimer

# Importez la classe FaceRecognition de votre module
from FaceRecognitionWithIndication import FaceRecognition


class AdminPage(QWidget):
    def __init__(self, face_recognition, name_display_widget):
        """
        Initialize the AdminPage widget.

        Args:
            face_recognition: An instance of the FaceRecognition class.
            name_display_widget: A QWidget for displaying names.
        """
        super().__init__()
        self.face_recognition = face_recognition
        self.name_display_widget = name_display_widget
        self.initUI()

    def initUI(self):
        """
        Initialize the user interface components of the AdminPage.
        """
        self.setWindowTitle("Admin Page")
        self.setGeometry(0, 0, 300, 150)
        self.center()

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.id_input = QLineEdit(self)
        self.id_input.setPlaceholderText("Enter ID")
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setPlaceholderText("Enter Password")
        verify_button = QPushButton("Verify")
        verify_button.clicked.connect(self.verify)

        layout.addWidget(self.id_input)
        layout.addWidget(self.password_input)
        layout.addWidget(verify_button)

        # Add click event handlers to show the virtual keyboard when the field is clicked.
        self.id_input.mousePressEvent = self.show_virtual_keyboard_id
        self.password_input.mousePressEvent = self.show_virtual_keyboard_password

    def verify(self):
        """
        Verify the entered ID and password.

        If the verification is successful, open the OptionsPage.
        Otherwise, display an error message.
        """
        entered_id = self.id_input.text()
        entered_password = self.password_input.text()

        if self.face_recognition.verify_id(entered_id, entered_password):
            self.open_options_page()
        else:
            QMessageBox.critical(self, "Access Denied", "Incorrect ID or password.")

    def open_options_page(self):
        """
        Open the OptionsPage and close the AdminPage.
        """
        self.options_page = OptionsPage(self.face_recognition, self.name_display_widget)
        self.options_page.setWindowTitle("Options Page")
        self.options_page.show()
        self.close()

    def center(self):
        """
        Center the widget on the screen.
        """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def show_virtual_keyboard_id(self, event):
        """
        Show the virtual keyboard for the ID input field.

        Args:
            event: The mousePressEvent event.
        """
        virtual_keyboard = VirtualKeyboard(self.id_input)
        virtual_keyboard.exec_()

    def show_virtual_keyboard_password(self, event):
        """
        Show the virtual keyboard for the password input field.

        Args:
            event: The mousePressEvent event.
        """
        virtual_keyboard = VirtualKeyboard(self.password_input)
        virtual_keyboard.exec_()

class OptionsPage(QWidget):
    def __init__(self, face_recognition, name_display_widget):
        """
        Initialize the OptionsPage widget.

        Args:
            face_recognition: An instance of the FaceRecognition class.
            name_display_widget: A QWidget for displaying names.
        """
        super().__init__()
        self.face_recognition = face_recognition
        self.name_display_widget = name_display_widget
        self.initUI()

    def initUI(self):
        """
        Initialize the user interface components of the OptionsPage.
        """
        self.setWindowTitle("Options Page")
        self.setGeometry(0, 0, 400, 50)
        self.center()

        layout = QVBoxLayout()
        self.setLayout(layout)

        register_button = QPushButton("Register")
        delete_button = QPushButton("Delete")

        register_button.clicked.connect(self.register)
        delete_button.clicked.connect(self.delete)

        layout.addWidget(register_button)
        layout.addWidget(delete_button)

    def register(self):
        """
        Open the RegistrationPage and close the OptionsPage.
        """
        self.registration_page = RegistrationPage(self.face_recognition, self.name_display_widget)
        self.registration_page.setWindowTitle("Registration Page")
        self.registration_page.show()
        self.close()

    def delete(self):
        """
        Open the DeletionPage and close the OptionsPage.
        """
        self.deletion_page = DeletionPage(self.face_recognition, self.name_display_widget)
        self.deletion_page.setWindowTitle("Deletion Page")
        self.deletion_page.show()
        self.close()

    def center(self):
        """
        Center the widget on the screen.
        """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
class RegistrationPage(QWidget):
    def __init__(self, face_recognition, name_display_widget):
        """
        Initialize the RegistrationPage widget.

        Args:
            face_recognition: An instance of the FaceRecognition class.
            name_display_widget: A QWidget for displaying names.
        """
        super().__init__()
        self.face_recognition = face_recognition
        self.name_display_widget = name_display_widget
        self.initUI()

    def initUI(self):
        """
        Initialize the user interface components of the RegistrationPage.
        """
        self.setWindowTitle("Registration Page")
        self.setGeometry(0, 0, 350, 150)
        self.center()

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Enter Name")
        self.last_name_input = QLineEdit(self)
        self.last_name_input.setPlaceholderText("Enter Last Name")
        self.apartment_number_input = QLineEdit(self)
        self.apartment_number_input.setPlaceholderText("Enter Apartment Number")
        self.house_admin_checkbox = QCheckBox("House administrator")  # Add the checkbox
        register_button = QPushButton("Register")
        register_button.clicked.connect(self.register)

        layout.addWidget(self.name_input)
        layout.addWidget(self.last_name_input)
        layout.addWidget(self.apartment_number_input)
        layout.addWidget(self.house_admin_checkbox)  # Add the checkbox
        layout.addWidget(register_button)

        # Add click event handlers to show the virtual keyboard when the field is clicked
        self.name_input.mousePressEvent = self.show_virtual_keyboard_name
        self.last_name_input.mousePressEvent = self.show_virtual_keyboard_last_name
        self.apartment_number_input.mousePressEvent = self.show_virtual_keyboard_apartment

    def register(self):
        """
        Register a person with the provided information.

        Retrieves the name, last name, apartment number, and house administrator status
        from the input fields, registers the person using FaceRecognition,
        displays a success message, and updates the name list in the name_display_widget.
        """
        name = self.name_input.text()
        last_name = self.last_name_input.text()
        apartment_number = self.apartment_number_input.text()
        is_house_admin = self.house_admin_checkbox.isChecked()  # Check if the checkbox is checked
        self.face_recognition.register_faces(name, last_name, apartment_number, is_house_admin)
        QMessageBox.information(self, "Registration Success", "Person successfully registered.")
        self.close()
        self.name_display_widget.update_name_list()

    def center(self):
        """
        Center the widget on the screen.
        """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def show_virtual_keyboard_name(self, event):
        """
        Show the virtual keyboard for the name input field.

        Args:
            event: The mousePressEvent event.
        """
        virtual_keyboard = VirtualKeyboard(self.name_input)
        virtual_keyboard.exec_()

    def show_virtual_keyboard_last_name(self, event):
        """
        Show the virtual keyboard for the last name input field.

        Args:
            event: The mousePressEvent event.
        """
        virtual_keyboard = VirtualKeyboard(self.last_name_input)
        virtual_keyboard.exec_()

    def show_virtual_keyboard_apartment(self, event):
        """
        Show the virtual keyboard for the apartment number input field.

        Args:
            event: The mousePressEvent event.
        """
        virtual_keyboard = VirtualKeyboard(self.apartment_number_input)
        virtual_keyboard.exec_()


class DeletionPage(QWidget):
    def __init__(self, face_recognition, name_display_widget):
        """
        Initialize the DeletionPage widget.

        Args:
            face_recognition: An instance of the FaceRecognition class.
            name_display_widget: A QWidget for displaying names.
        """
        super().__init__()
        self.face_recognition = face_recognition
        self.name_display_widget = name_display_widget
        self.initUI()

    def initUI(self):
        """
        Initialize the user interface components of the DeletionPage.
        """
        self.setWindowTitle("Deletion Page")
        self.setGeometry(0, 0, 350, 150)
        self.center()

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Enter Name")
        self.last_name_input = QLineEdit(self)
        self.last_name_input.setPlaceholderText("Enter Last Name")
        self.apartment_number_input = QLineEdit(self)
        self.apartment_number_input.setPlaceholderText("Enter Apartment Number")
        self.house_admin_checkbox = QCheckBox("House administrator")  # Add the checkbox
        delete_button = QPushButton("Delete")
        delete_button.clicked.connect(self.delete)

        layout.addWidget(self.name_input)
        layout.addWidget(self.last_name_input)
        layout.addWidget(self.apartment_number_input)
        layout.addWidget(self.house_admin_checkbox)  # Add the checkbox
        layout.addWidget(delete_button)

        # Add click event handlers to show the virtual keyboard when the field is clicked
        self.name_input.mousePressEvent = self.show_virtual_keyboard_name
        self.last_name_input.mousePressEvent = self.show_virtual_keyboard_last_name
        self.apartment_number_input.mousePressEvent = self.show_virtual_keyboard_apartment

    def delete(self):
        """
        Delete a person based on the provided information.

        Retrieves the name, last name, apartment number, and house administrator status
        from the input fields, deletes the person using FaceRecognition,
        displays a success or failure message, and updates the name list in the name_display_widget.
        """
        name = self.name_input.text()
        last_name = self.last_name_input.text()
        apartment_number = self.apartment_number_input.text()
        is_house_admin = self.house_admin_checkbox.isChecked()  # Check if the checkbox is checked
        result = self.face_recognition.delete_person(name, last_name, apartment_number, is_house_admin)
        if result:
            QMessageBox.information(self, "Deletion Success", "Person successfully deleted.")
        else:
            QMessageBox.critical(self, "Deletion Failed", "Person not found or deletion failed.")
        self.close()
        self.name_display_widget.update_name_list()

    def center(self):
        """
        Center the widget on the screen.
        """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def show_virtual_keyboard_name(self, event):
        """
        Show the virtual keyboard for the name input field.

        Args:
            event: The mousePressEvent event.
        """
        virtual_keyboard = VirtualKeyboard(self.name_input)
        virtual_keyboard.exec_()

    def show_virtual_keyboard_last_name(self, event):
        """
        Show the virtual keyboard for the last name input field.

        Args:
            event: The mousePressEvent event.
        """
        virtual_keyboard = VirtualKeyboard(self.last_name_input)
        virtual_keyboard.exec_()

    def show_virtual_keyboard_apartment(self, event):
        """
        Show the virtual keyboard for the apartment number input field.

        Args:
            event: The mousePressEvent event.
        """
        virtual_keyboard = VirtualKeyboard(self.apartment_number_input)
        virtual_keyboard.exec_()


class NameDisplayWidget(QWidget):
    def __init__(self, face_recognition):
        """
        Initialize the NameDisplayWidget.

        Args:
            face_recognition: An instance of the FaceRecognition class.
        """
        super().__init__()
        self.face_recognition = face_recognition

        self.layout = QHBoxLayout(self)

        self.prev_button = QPushButton("<")
        self.prev_button.clicked.connect(self.show_previous_name)
        self.layout.addWidget(self.prev_button)

        self.name_field = QLineEdit()
        self.name_field.setReadOnly(True)
        self.name_field.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.name_field)

        self.next_button = QPushButton(">")
        self.next_button.clicked.connect(self.show_next_name)
        self.layout.addWidget(self.next_button)

        self.current_name_index = 0
        self.registered_names = list(self.face_recognition.house_administrator_dict.keys())

        self.update_name_display()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_name_display)
        self.timer.start(1000)

    def update_name_list(self):
        """
        Update the list of registered names.
        """
        self.registered_names = list(self.face_recognition.house_administrator_dict.keys())
        self.current_name_index = 0
        self.update_name_display()

    def update_name_display(self):
        """
        Update the displayed name in the widget.
        """
        if not self.registered_names:
            self.name_field.setText("No names registered")
            return

        current_name = self.registered_names[self.current_name_index]
        # Remove any digits at the end of the name (if any)
        current_name = ''.join(filter(lambda x: not x.isdigit(), current_name))
        # Replace underscores with spaces
        current_name = current_name.replace("_", " ")

        self.name_field.setText(current_name)

    def show_previous_name(self):
        """
        Display the previous name in the list.
        """
        if not self.registered_names:
            return
        self.current_name_index = (self.current_name_index - 1) % len(self.registered_names)
        self.update_name_display()

    def show_next_name(self):
        """
        Display the next name in the list.
        """
        if not self.registered_names:
            return
        self.current_name_index = (self.current_name_index + 1) % len(self.registered_names)
        self.update_name_display()


class VirtualKeyboard(QDialog):
    def __init__(self, target_input):
        """
        Initialize the VirtualKeyboard dialog.

        Args:
            target_input: The input field to which the virtual keyboard inputs characters.
        """
        super().__init__()
        self.target_input = target_input
        self.setWindowTitle("Virtual Keyboard")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Add a frame at the bottom of the screen for the virtual keyboard
        self.keyboard_frame = QFrame()
        self.keyboard_frame.setFrameShape(QFrame.StyledPanel)
        self.keyboard_layout = QGridLayout(self.keyboard_frame)

        buttons = [
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
            'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
            'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
            'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Backspace', 'Space', 'Enter'
        ]

        row, col = 0, 0
        for button_text in buttons:
            button = QPushButton(button_text)
            button.clicked.connect(self.button_click)
            self.keyboard_layout.addWidget(button, row, col)
            col += 1
            if col > 9:
                col = 0
                row += 1

        self.layout.addWidget(self.keyboard_frame)
        self.keyboard_frame.hide()  # By default, hide the virtual keyboard

    def button_click(self):
        """
        Handle button clicks on the virtual keyboard.

        Depending on the clicked button, insert characters, delete characters, add a space,
        or accept the input.
        """
        button = self.sender()
        text = button.text()
        if text == 'Backspace':
            current_text = self.target_input.text()
            self.target_input.setText(current_text[:-1])
        elif text == 'Space':
            current_text = self.target_input.text()
            self.target_input.setText(current_text + ' ')
        elif text == 'Enter':
            self.accept()
        else:
            current_text = self.target_input.text()
            self.target_input.setText(current_text + text)

    def showEvent(self, event):
        """
        Show the virtual keyboard when the input field is selected.

        Args:
            event: The showEvent event.
        """
        self.keyboard_frame.show()

    def hideEvent(self, event):
        """
        Hide the virtual keyboard when the input field loses focus.

        Args:
            event: The hideEvent event.
        """
        self.keyboard_frame.hide()


class MainWindow(QMainWindow):
    def __init__(self, face_recognition):
        """
        Initialize the main application window.

        Args:
            face_recognition: An instance of the FaceRecognition class.
        """
        super().__init__()
        self.face_recognition = face_recognition
        self.initUI()

    def initUI(self):
        """
        Initialize the user interface components of the main window.
        """
        self.setWindowTitle('VisiaScan')
        screen = QDesktopWidget().screenGeometry()

        self.setGeometry(0, 0, screen.width(), screen.height())
        self.setWindowFlags(Qt.CustomizeWindowHint)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMinimizeButtonHint)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        pixmap = QPixmap("background.jpg")
        background_label = QLabel(central_widget)
        background_label.setPixmap(pixmap)
        background_label.setGeometry(0, 0, screen.width(), screen.height())

        central_layout = QVBoxLayout(central_widget)

        # Add the name display widget just above the "Sonner" button
        self.name_display_widget = NameDisplayWidget(self.face_recognition)
        central_layout.addWidget(self.name_display_widget, alignment=Qt.AlignCenter)

        button_layout = QHBoxLayout()

        self.admin_button = QPushButton("Admin")
        self.admin_button.clicked.connect(self.open_admin_page)
        button_layout.addWidget(self.admin_button, alignment=Qt.AlignLeft | Qt.AlignBottom)
        button_layout.addStretch(1)

        self.sonner_button = QPushButton("Sonner")
        self.sonner_button.clicked.connect(self.ring_action)
        central_layout.addWidget(self.sonner_button, alignment=Qt.AlignHCenter | Qt.AlignBottom)
        central_layout.addLayout(button_layout)

    def open_admin_page(self):
        """
        Open the Admin Page when the "Admin" button is clicked.
        """
        self.admin_page = AdminPage(self.face_recognition, self.name_display_widget)
        self.admin_page.setWindowTitle("Admin Page")
        self.admin_page.show()

    def ring_action(self):
        # Add your code for what happens when the "Ring" button is clicked
        pass


def main():
    app = QApplication(sys.argv)
    face_recognition = FaceRecognition()
    window = MainWindow(face_recognition)
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
