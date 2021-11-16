import sys
from random import randint

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from UI import UI

SCREEN_SIZE = [500, 500]


def parse(n: int) -> str:
    h = '0123456789ABCDEF'
    s = ''
    while n > 0:
        s = h[n % 16] + s
        n = n // 16
    return s


def generate_random_color():
    r, g, b = randint(50, 255), randint(50, 255), randint(50, 255)
    return f'#{parse(r)}{parse(g)}{parse(b)}'


class Circle:
    def __init__(self, x, y, r, color):
        self.x = x
        self.y = y
        self.r = r
        self.color = color

    def get_parameters(self):
        return self.x, self.y, self.r, self.r


class DrawStar(UI):
    signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.initUI()
        self.initUI()
        self.btn.clicked.connect(self.btn_pushed)
        self.circles = []

    def btn_pushed(self):
        self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_star(qp)
        qp.end()

    def draw_star(self, qp):
        size = randint(50, 200)
        x, y = randint(size, SCREEN_SIZE[0] - size), randint(size, SCREEN_SIZE[1] - size)
        color = QColor(generate_random_color())
        self.circles.append(Circle(x, y, size, color))
        for circle in self.circles:
            qp.setBrush(QBrush(QColor(circle.color), Qt.SolidPattern))
            qp.drawEllipse(*circle.get_parameters())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DrawStar()
    ex.show()
    sys.exit(app.exec())
