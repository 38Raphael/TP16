from PySide2.QtWidgets import QWidget, QHBoxLayout, QProgressBar, QSlider, QApplication


class Wind(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.layout = QHBoxLayout()
        self.setWindowTitle("IHM")

        self.w1 = QProgressBar()
        self.w2 = QSlider()

        self.layout.addWidget(self.w1)
        self.layout.addWidget(self.w2)
        self.w2.valueChanged.connect(self.clicked)

        self.setLayout(self.layout)

    def clicked(self):
        self.w1.setValue(self.w2.value())


if __name__ == "__main__":
    app = QApplication([])
    win = Wind()
    win.show()
    app.exec_()
