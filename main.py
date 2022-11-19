import sys
import random

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic


class YellowCircle(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.run)
        self.setFixedSize(self.size())

    def run(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def draw_circle(self, qp):
        d = random.randint(10, 200)
        x, y = random.randint(1, self.width() - d // 2), random.randint(1, self.height() - d // 2)
        qp.setBrush(QColor('yellow'))
        qp.drawEllipse(x, y, d, d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YellowCircle()
    ex.show()
    sys.exit(app.exec())
