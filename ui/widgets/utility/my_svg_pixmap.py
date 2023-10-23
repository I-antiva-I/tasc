from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtCore import QFile, QByteArray
from PyQt5.QtGui import QPainter, QFontMetrics, QPixmap, QColor
from PyQt5.QtSvg import QSvgRenderer
from PyQt5.QtWidgets import QSizePolicy, QLabel
from PyQt5.QtXml import QDomDocument, QDomElement


def create_svg_pixmap(path_to_icon, icon_width=32, icon_height=32, icon_color="#000000"):
    # File
    file = QFile(path_to_icon)
    file.open(QtCore.QIODevice.ReadOnly)

    # Data
    data = QByteArray(file.readAll())
    svg_document = QDomDocument()
    svg_document.setContent(data)
    set_attribute(svg_document.documentElement(), "path", "fill", icon_color)

    # Pixmap
    pixmap = QPixmap()
    pixmap.loadFromData(svg_document.toByteArray(), "SVG")
    return pixmap.scaled(icon_width, icon_height, Qt.Qt.KeepAspectRatio, Qt.Qt.SmoothTransformation)


# Set attribute value for SVG tag
def set_attribute(element: QDomElement, tag_name, attribute_name, attribute_value, use_recursion=True):
    if element.tagName() == tag_name:
        element.setAttribute(attribute_name, attribute_value)

    if use_recursion:
        for i in range(element.childNodes().count()):
            if element.childNodes().at(i).isElement():
                set_attribute(element.childNodes().at(i).toElement(), tag_name, attribute_name, attribute_value)
