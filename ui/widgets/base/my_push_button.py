from enum import Enum

from PyQt5 import QtWidgets, QtGui, Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QColor, QIcon, QPixmap, QMouseEvent
from PyQt5.QtWidgets import QPushButton

from ui.widgets.utility.my_svg_pixmap import create_svg_pixmap
from ui.widgets.utility.my_widget import MyWidget


class MyPushButton(QPushButton, MyWidget):
    def __init__(self, text="Default text", name=None):
        super(MyPushButton, self).__init__()

        # ID
        if name is not None:
            self.setObjectName(name)

        self.setText(text)
        self.setCursor(Qt.Qt.PointingHandCursor)

