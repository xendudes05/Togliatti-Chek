import sys
from random import randint
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QPointF
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt6 import uic


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui.ui', self)
        self.setWindowTitle('Рисование')

        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_flag(self, qp):
        red = randint(0, 255)
        green = randint(0, 255)
        blue = randint(0, 255)
        qp.setBrush(QColor(red, green, blue))
        r = randint(20, 150)
        x = randint(0, self.width() - r)
        y = randint(0, self.height() - r)
        qp.drawEllipse(QPointF(x, y), r / 2, r / 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
