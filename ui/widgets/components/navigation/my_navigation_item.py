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
    icon_color_default = "#424242"
    icon_color_hovered = "#4169E1"
    icon_color_active =  "#FF7A00"

    def __init__(self, key, header, navigation):
        super(MyNavigationItem, self).__init__(layout=QtWidgets.QHBoxLayout())

        self.item_icon = MySVGIcon(path_to_icon=icon_path_from_key(key))
        self.item_label = MyLabel(text=header)

        self.item_icon.set_style_class("nav-item__icon")
        self.item_label.set_style_class("nav-item__label")
        self.set_style_class("nav-item")

        self.navigation = navigation
        self.item_key = key
        self.item_state = None
        self.set_state(MyNavigationItemState.DEFAULT)

        self.place_all(self.item_icon, self.item_label)

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
            self.setFocusPolicy(Qt.Qt.FocusPolicy.TabFocus)
            self.toggle_style_class("nav-item--active", False, False)
            self.toggle_style_class("nav-item--hovered", False, False)
            self.toggle_style_class("nav-item--default", True, True)
            self.item_icon.reset_pixmap(MyNavigationItem.icon_color_default)

        elif state == MyNavigationItemState.HOVERED:
            self.toggle_style_class("nav-item--default", False, False)
            self.toggle_style_class("nav-item--active", False, False)
            self.toggle_style_class("nav-item--hovered", True, True)
            self.setCursor(Qt.Qt.PointingHandCursor)
            self.item_icon.reset_pixmap(MyNavigationItem.icon_color_hovered)

        elif state == MyNavigationItemState.ACTIVE:
            self.setFocusPolicy(Qt.Qt.FocusPolicy.NoFocus)
            self.toggle_style_class("nav-item--default", False, False)
            self.toggle_style_class("nav-item--hovered", False, False)
            self.toggle_style_class("nav-item--active", True, True)
            self.item_icon.reset_pixmap(MyNavigationItem.icon_color_active)

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
