from PyQt5 import QtWidgets, QtGui
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QPushButton

from ui.widgets.utility.my_widget import MyWidget


class MyPushButton(QPushButton, MyWidget):
    def __init__(self, text="Default text"):
        super(MyPushButton, self).__init__()

        self.setText(text)
