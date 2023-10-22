from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtGui import QPainter, QFontMetrics
from PyQt5.QtWidgets import QSizePolicy

from ui.widgets.utility.my_widget import MyWidget


class MyLabel(QtWidgets.QLabel, MyWidget):
    def __init__(self, name=None, text="Placeholder text"):
        super(MyLabel, self).__init__()

        if name is not None:
            self.setObjectName(name)
        self.setText(text)

