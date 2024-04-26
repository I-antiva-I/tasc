from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QSizePolicy

from ui.widgets.base.my_panel import MyPanel
from ui.widgets.components.navigation.my_navigation_item import MyNavigationItem, MyNavigationItemState
from ui.widgets.utility.my_widget_with_layout import Alignment


class MyNavigation(MyPanel):
    def __init__(self, change_active_panel):
        super(MyNavigation, self).__init__(layout=QtWidgets.QVBoxLayout())

        # Buttons for sub-panels
        self.navigation_items = {}
        self.active_item_key = None
        self.change_active_panel = lambda panel_key: change_active_panel(panel_key)

        self.set_style_class("navigation")
        self.set_spacing(8)
        self.set_alignment(Alignment.TOP)
        self.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)

    def on_item_clicked(self, item_key):
        # Change the state of the previous item
        if self.active_item_key is not None:
            self.navigation_items[self.active_item_key].set_state(MyNavigationItemState.DEFAULT)

        self.active_item_key = item_key

        # Set the state of the new item
        self.navigation_items[self.active_item_key].set_state(MyNavigationItemState.ACTIVE)

        self.change_active_panel(item_key)

    def add_navigation_item(self, key, header):
        self.navigation_items[key] = MyNavigationItem(key, header, self)
        self.place(self.navigation_items[key])