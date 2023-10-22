from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtCore import QFile, QByteArray
from PyQt5.QtGui import QPainter, QFontMetrics, QPixmap, QColor
from PyQt5.QtSvg import QSvgRenderer
from PyQt5.QtWidgets import QSizePolicy, QLabel
from PyQt5.QtXml import QDomDocument, QDomElement

from ui.widgets.utility.my_widget import MyWidget


class MySVGIcon(QLabel, MyWidget):
    def __init__(self, path_to_icon, width=32, height=32, icon_color="#000000"):
        super(MySVGIcon, self).__init__()

        self.path_to_icon = path_to_icon
        self.image_width = width
        self.image_height = height

        self.reset_pixmap(icon_color)

        self.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)

    # Read SVG, apply specified color, and reload pixmap
    def reset_pixmap(self, icon_color="#000000"):
        # File
        file = QFile(self.path_to_icon)
        file.open(QtCore.QIODevice.ReadOnly)

        # Data
        data = QByteArray(file.readAll())
        svg_document = QDomDocument()
        svg_document.setContent(data)
        set_attribute(svg_document.documentElement(), "path", "fill", icon_color)

        # Pixmap
        pixmap = QPixmap()
        pixmap.loadFromData(svg_document.toByteArray(), "SVG")
        pixmap = pixmap.scaled(self.image_width, self.image_height, Qt.Qt.KeepAspectRatio, Qt.Qt.SmoothTransformation)
        self.setPixmap(pixmap)


# Set attribute value for SVG tag
def set_attribute(element: QDomElement, tag_name, attribute_name, attribute_value, use_recursion=True):
    if element.tagName() == tag_name:
        element.setAttribute(attribute_name, attribute_value)

    if use_recursion:
        for i in range(element.childNodes().count()):
            if element.childNodes().at(i).isElement():
                set_attribute(element.childNodes().at(i).toElement(), tag_name, attribute_name, attribute_value)
