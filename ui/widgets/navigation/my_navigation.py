from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QSizePolicy

from ui.widgets.basic.my_panel import MyPanel
from ui.widgets.navigation.my_navigation_item import MyNavigationItem
from ui.widgets.utility.my_widget_with_layout import Alignment


class MyNavigation(MyPanel):
    def __init__(self, change_active_panel):
        super(MyNavigation, self).__init__(layout=QtWidgets.QVBoxLayout())

        self.set_class("navigation")
        self.set_alignment(Alignment.TOP)
        self.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        self.navigation_items = {}
        self.change_active_panel = change_active_panel
        self.set_spacing(8)

    def add_navigation_item(self, key, header, icon=None):
        self.navigation_items[key] = MyNavigationItem(key, header, self)
        self.place(self.navigation_items[key])