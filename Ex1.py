from PySide2.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QApplication
from numpy import random


class Pannel(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.layout = QVBoxLayout()
        self.setWindowTitle("Cycles de l'ISEN Yncréa Ouest")
        self.setFixedSize(500, 300)

        self.w1 = QLabel("CSI")
        self.w2 = QPushButton("Changer le cycle")

        self.layout.addWidget(self.w1)
        self.layout.addWidget(self.w2)
        self.w2.clicked.connect(self.click)

        self.setLayout(self.layout)

    def click(self):
        loste = ["CSI", "CIR", "BIOST", "CENT", "BIAST", "EST"]
        newfil = random.choice(loste)
        self.w1.setText(newfil)


if __name__ == "__main__":
    app = QApplication([])
    win = Pannel()
    win.show()
    app.exec_()
