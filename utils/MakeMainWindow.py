from PyQt6.QtWidgets import QMainWindow, QWidget, QSizePolicy


class MainWindow(QWidget):
    def __init__(self,
                 center=True,
                 title="title",
                 x=100, y=100,
                 w=800, h=600):
        super().__init__()
        self.setGeometry(x, y, w, h)
        self.setWindowTitle(title)
        self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)