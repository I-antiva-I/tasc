from enum import Enum

from PyQt5 import QtWidgets, Qt

from ui.widgets.base.my_svg_icon import MySVGIcon
from ui.widgets.base.my_label import MyLabel
from ui.widgets.base.my_panel import MyPanel


class MyNavigationItemState(Enum):
    DEFAULT = 1
    HOVERED = 2
    ACTIVE = 3


class MyNavigationItem(MyPanel):
    def __init__(self, key, header, navigation):
        super(MyNavigationItem, self).__init__(layout=QtWidgets.QHBoxLayout())

        self.item_icon = MySVGIcon(path_to_icon=icon_path_from_key(key))
        self.item_label = MyLabel(text=header)

        self.place_all(self.item_icon, self.item_label)

        self.item_icon.set_class("nav-item__icon")
        self.item_label.set_class("nav-item__label")
        self.set_class("nav-item")

        self.navigation = navigation
        self.item_key = key
        self.item_state = None
        self.set_state(MyNavigationItemState.DEFAULT)

    def mousePressEvent(self, QEvent):
        super().mousePressEvent(QEvent)
        self.navigation.on_item_clicked(self.item_key)

    def enterEvent(self, QEvent):
        super().enterEvent(QEvent)
        if self.item_state != MyNavigationItemState.ACTIVE:
            self.set_state(MyNavigationItemState.HOVERED)

    def leaveEvent(self, QEvent):
        super().leaveEvent(QEvent)
        if self.item_state != MyNavigationItemState.ACTIVE:
            self.set_state(MyNavigationItemState.DEFAULT)

    def set_state(self, state):
        if state == MyNavigationItemState.DEFAULT:
            self.toggle_class("nav-item--active", False, False)
            self.toggle_class("nav-item--hovered", False, False)
            self.toggle_class("nav-item--default", True, True)
            self.item_icon.reset_pixmap("#424242")
        elif state == MyNavigationItemState.HOVERED:
            self.toggle_class("nav-item--default", False, False)
            self.toggle_class("nav-item--active", False, False)
            self.toggle_class("nav-item--hovered", True, True)
            self.setCursor(Qt.Qt.PointingHandCursor)
            self.item_icon.reset_pixmap("dodgerblue")
        elif state == MyNavigationItemState.ACTIVE:
            self.toggle_class("nav-item--default", False, False)
            self.toggle_class("nav-item--hovered", False, False)
            self.toggle_class("nav-item--active", True, True)
            self.item_icon.reset_pixmap("seagreen")

        self.item_state = state


def icon_path_from_key(key):
    root = "./ui/assets/images/navigation/"

    if key == "documents":
        return root+"document.svg"
    elif key == "query":
        return root+"pen.svg"
    elif key == "results":
        return root+"flask.svg"
    elif key == "settings":
        return root+"gear.svg"
    else:
        return root+"question.svg"
