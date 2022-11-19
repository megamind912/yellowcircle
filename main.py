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
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(self.width() // 2 - d // 2, self.height() // 2 - d // 2, d, d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YellowCircle()
    ex.show()
    sys.exit(app.exec())
