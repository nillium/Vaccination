from PyQt6.QtWidgets import QPushButton


class MakeButton(QPushButton):

    def __init__(self, button_text,
                 call_on_press,
                 x=10, y=10,
                 w=100, h=20,
                 parent=None):
        super().__init__()
        self.call_on_press = call_on_press
        self.setText(button_text)
        self.setGeometry(x, y, w, h)
        self.clicked.connect(self.call_on_press)
