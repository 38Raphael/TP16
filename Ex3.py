from PySide2.QtWidgets import QWidget, QVBoxLayout, QPushButton, QApplication


class Pannel(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.layout = QVBoxLayout()
        self.setWindowTitle("IHM")
        self.setFixedSize(300, 200)
        self.compteur = 1

        self.w1 = QPushButton("Changer mon texte!")

        self.layout.addWidget(self.w1)
        self.w1.clicked.connect(self.click)

        self.setLayout(self.layout)

    def click(self):
        print("clic " + str(self.compteur))
        self.w1.setText("clic " + str(self.compteur))
        self.compteur += 1





if __name__ == "__main__":
    app = QApplication([])
    win = Pannel()
    win.show()
    app.exec_()
