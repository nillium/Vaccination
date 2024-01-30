from PyQt6.QtWidgets import QLabel, QSizePolicy
from PyQt6.QtCore import Qt


class MakeLabel(QLabel):

    def __init__(self, label_text, x=10, y=10, w=200, h=20, align="c", parent=None, size_policy="expanding"):
        super().__init__(parent)

        self.setText(label_text)


        if size_policy == "expanding":
            self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        if size_policy == "fixed":
            self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
            self.setFixedHeight(h)

        if align == "c":
            self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        if align == "l":
            self.setAlignment(Qt.AlignmentFlag.AlignLeft)
        if align == "r":
            self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setStyleSheet("background-color: #eeeeee;\
                                border: 0px solid #ff00aa;\
                                padding: 0px;")

        # self.setGeometry(x, y, w, h)
