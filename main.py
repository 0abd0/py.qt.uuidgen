# pip install pyqt5

import sys
import uuid
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget, QMessageBox


class UUIDGeneratorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Create layout
        layout = QVBoxLayout()

        # Create widgets
        self.input_field = QLineEdit(self)

        self.input_field.setPlaceholderText("Enter number of UUIDs to generate")

        self.generate_button = QPushButton("Generate UUIDs", self)
        self.generate_button.clicked.connect(self.generate_uuids)

        self.uuid_list = QListWidget(self)

        # Add widgets to layout
        layout.addWidget(self.input_field)
        layout.addWidget(self.generate_button)
        layout.addWidget(self.uuid_list)

        # Set layout to the window
        self.setLayout(layout)

        # Window settings
        self.setWindowTitle('UUID Generator___0abd0___')
        self.setGeometry(300, 300, 400, 300)

    def generate_uuids(self):
        try:
            num_uuids = int(self.input_field.text())
            if num_uuids <= 0:
                raise ValueError("Number must be positive")

            self.uuid_list.clear()
            for _ in range(num_uuids):
                new_uuid = uuid.uuid4()
                self.uuid_list.addItem(str(new_uuid))
        except ValueError as ve:
            QMessageBox.critical(self, 'Invalid Input', str(ve))


def main():
    app = QApplication(sys.argv)
    ex = UUIDGeneratorApp()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
