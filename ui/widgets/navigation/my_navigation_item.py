from PyQt5 import QtWidgets

from ui.widgets.basic.my_image import MyImage
from ui.widgets.basic.my_label import MyLabel
from ui.widgets.basic.my_panel import MyPanel
from ui.widgets.utility.my_widget_interactive import MyWidgetInteractive


class MyNavigationItem(MyPanel , MyWidgetInteractive):
    def __init__(self, key, header, navigation):
        super(MyNavigationItem, self).__init__(layout=QtWidgets.QHBoxLayout())

        self.item_icon = MyImage(path_to_image="./ui/assets/images/circle-question-solid.svg")
        self.item_label = MyLabel(text=header)

        self.place_all(self.item_icon, self.item_label)

        self.item_icon.set_class("nav-item__icon")
        self.item_label.set_class("nav-item__label")
        self.set_class("nav-item")

        self.on_mouse_click_event = lambda: navigation.change_active_panel(key)
