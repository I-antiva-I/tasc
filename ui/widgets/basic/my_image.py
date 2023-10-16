from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtGui import QPainter, QFontMetrics, QPixmap
from PyQt5.QtSvg import QSvgRenderer
from PyQt5.QtWidgets import QSizePolicy, QLabel

from ui.widgets.utility.my_widget import MyWidget


class MyImage(QLabel, MyWidget):
    def __init__(self, path_to_image, width=32, height=32):
        super(MyImage, self).__init__()

        pixmap = QPixmap(path_to_image)
        pixmap = pixmap.scaled(width, height, Qt.Qt.KeepAspectRatio, Qt.Qt.SmoothTransformation)
        self.setPixmap(pixmap)
        self.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
