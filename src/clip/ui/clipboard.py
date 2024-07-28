import sys
from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton
from PySide6.QtGui import QClipboard


class ClipboardApp(QWidget):
    def __init__(self, data):
        super().__init__()
        self.pairs = data
        self.init_ui()

    def init_ui(self):
        layout = QGridLayout()

        # Create buttons for each pair
        for i, (label, value) in enumerate(self.pairs):
            row = i
            button = QPushButton(label, self)
            button.clicked.connect(lambda checked, val=label: self.copy_to_clipboard(val))
            layout.addWidget(button, row, 0)
            button = QPushButton(value, self)
            button.clicked.connect(lambda checked, val=value: self.copy_to_clipboard(val))
            layout.addWidget(button, row, 1)

        self.setLayout(layout)
        self.setWindowTitle('Clip')
        self.show()

    def copy_to_clipboard(self, value):
        clipboard = QApplication.clipboard()
        clipboard.setText(value)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ClipboardApp()
    sys.exit(app.exec_())