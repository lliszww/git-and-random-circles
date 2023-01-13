import random
import sys
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication
from Ui import Ui_Form


class Example(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw(self, qp):
        rad = random.randint(10, 150)
        x = random.randint(10, 250)
        y = random.randint(10, 250)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        qp.setPen(QColor(r, g, b))
        qp.drawEllipse(x, y, 2 * rad, 2 * rad)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())