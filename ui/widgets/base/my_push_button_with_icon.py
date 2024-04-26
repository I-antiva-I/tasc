from enum import Enum

from PyQt5 import QtWidgets, QtGui, Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QColor, QIcon, QPixmap, QMouseEvent
from PyQt5.QtWidgets import QPushButton

from ui.widgets.utility.my_svg_pixmap import create_svg_pixmap
from ui.widgets.utility.my_widget import MyWidget


class MyPushButtonIcon(Enum):
    COPY = 1
    PASTE = 2
    CLEAR = 3
    EXPORT = 4
    CALCULATE = 5
    FILE = 6
    FOLDER = 7
    REMOVE = 8


class MyPushButtonWithIcon(QPushButton, MyWidget):
    def __init__(self, text="Default text", name=None,
                 icon_type=0, icon_width=28, icon_height=28,
                 icon_offset_x=12, icon_offset_y=0,
                 icon_color_default="#343434", icon_color_hovered="#4169E1", icon_color_pressed="#FF7A00"):
        super(MyPushButtonWithIcon, self).__init__()

        # Identifier
        if name is not None:
            self.setObjectName(name)

        # Margins
        self.pixmap_offset = QSize(icon_offset_x, icon_offset_y)

        # Icon settings
        self.icon_width = icon_width
        self.icon_height = icon_height
        self.icon_type = icon_type
        self.icon_color_default = icon_color_default
        self.icon_color_hovered = icon_color_hovered
        self.icon_color_pressed = icon_color_pressed

        # Pixel map
        self.pixmap = None
        self.reset_pixmap(self.icon_color_default)

        # Misc
        self.setText(text)
        self.setCursor(Qt.Qt.PointingHandCursor)
        self.setMinimumSize(self.sizeHint())

    # Reload pixmap
    def reset_pixmap(self, icon_color="#000000"):
        self.pixmap = create_svg_pixmap(icon_path_from_type(self.icon_type), self.icon_width, self.icon_height, icon_color)

    def mousePressEvent(self, QEvent):
        self.reset_pixmap(self.icon_color_pressed)
        super().mousePressEvent(QEvent)

    def mouseReleaseEvent(self, QEvent:QMouseEvent):
        if not (abs(self.height() - QEvent.pos().y()) > self.height() or abs(self.width() - QEvent.pos().x()) > self.width()):
            self.reset_pixmap(self.icon_color_hovered)
        super().mouseReleaseEvent(QEvent)

    def enterEvent(self, QEvent):
        self.reset_pixmap(self.icon_color_hovered)
        super().enterEvent(QEvent)

    def leaveEvent(self, QEvent):
        self.reset_pixmap(self.icon_color_default)
        super().leaveEvent(QEvent)

    def sizeHint(self):
        parent_size = QtWidgets.QPushButton.sizeHint(self)
        icon_size = self.pixmap.size()
        return QtCore.QSize(parent_size.width() + icon_size.width()*2 + self.pixmap_offset.width()*3,
                            max(parent_size.height(), icon_size.height() + self.pixmap_offset.height()*2))

    def paintEvent(self, QEvent):
        QtWidgets.QPushButton.paintEvent(self, QEvent)

        position_x = self.pixmap_offset.width()
        position_y =  (self.height() - self.pixmap.height())/2 + self.pixmap_offset.height()

        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
        painter.setRenderHint(QtGui.QPainter.SmoothPixmapTransform, True)
        painter.drawPixmap(int(position_x), int(position_y), self.pixmap)


def icon_path_from_type(icon_type):
    root = "./ui/assets/images/button/"

    # Document group
    if icon_type == MyPushButtonIcon.FILE:
        return root+"file.svg"
    elif icon_type == MyPushButtonIcon.FOLDER:
        return root+"folder.svg"
    elif icon_type == MyPushButtonIcon.REMOVE:
        return root+"remove.svg"
    elif icon_type == MyPushButtonIcon.CALCULATE:
        return root+"calculate.svg"
    # Query group
    elif icon_type == MyPushButtonIcon.CLEAR:
        return root+"clear.svg"
    elif icon_type == MyPushButtonIcon.COPY:
        return root+"copy.svg"
    elif icon_type == MyPushButtonIcon.PASTE:
        return root+"paste.svg"
    #
    elif icon_type == MyPushButtonIcon.EXPORT:
        return root+"export.svg"
    #
    else:
        return ""
