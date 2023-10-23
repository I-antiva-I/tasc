from PyQt5 import QtCore, Qt
from PyQt5.QtCore import QFile, QByteArray
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QSizePolicy, QLabel
from PyQt5.QtXml import QDomDocument, QDomElement

from ui.widgets.utility.my_svg_pixmap import create_svg_pixmap
from ui.widgets.utility.my_widget import MyWidget


class MySVGIcon(QLabel, MyWidget):
    def __init__(self, path_to_icon, icon_width=32, icon_height=32, icon_color="#000000"):
        super(MySVGIcon, self).__init__()

        self.path_to_icon = path_to_icon
        self.icon_width = icon_width
        self.icon_height = icon_height

        self.reset_pixmap(icon_color)

        self.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)

    # Reload pixmap
    def reset_pixmap(self, icon_color="#000000"):
        self.setPixmap(create_svg_pixmap(self.path_to_icon, self.icon_width, self.icon_height, icon_color))
