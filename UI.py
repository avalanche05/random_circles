from PyQt5.QtWidgets import QWidget, QPushButton

SCREEN_SIZE = [500, 500]


class UI(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.btn = QPushButton(self)

    def initUI(self):
        self.setFixedSize(*SCREEN_SIZE)
        self.setWindowTitle('Случайные окружности')
