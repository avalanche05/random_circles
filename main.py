import sys
from math import cos, pi, sin
from random import randint
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPainter, QPen, QBrush, QPalette
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton

SCREEN_SIZE = [500, 500]
# Задаём длину стороны и количество углов
SIDE_LENGTH = 200
SIDES_COUNT = 5


class DrawStar(QWidget):
    signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setFixedSize(*SCREEN_SIZE)
        self.initUI()
        self.btn = QPushButton(self)
        self.btn.clicked.connect(self.btn_pushed)

    def btn_pushed(self):
        self.update()

    def initUI(self):
        self.setGeometry(300, 300, *SCREEN_SIZE)
        self.setWindowTitle('Рисуем звезду')

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_star(qp)
        qp.end()

    def draw_star(self, qp):
        size = randint(50, 200)
        x, y = randint(100, SCREEN_SIZE[0] - size), randint(100, SCREEN_SIZE[1] - size)
        qp.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
        qp.drawEllipse(x, y, size, size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DrawStar()
    ex.show()
    sys.exit(app.exec())
