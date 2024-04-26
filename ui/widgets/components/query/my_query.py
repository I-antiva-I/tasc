from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPlainTextEdit

from ui.widgets.base.my_group import MyGroup
from ui.widgets.base.my_panel import MyPanel
from ui.widgets.base.my_push_button_with_icon import MyPushButtonWithIcon, MyPushButtonIcon


class MyQuery(MyPanel):
    def __init__(self):
        super(MyQuery, self).__init__(layout=QtWidgets.QVBoxLayout())

        self.text_area = QPlainTextEdit()
        self.place(self.text_area)

        # Query control
        panel_control = MyPanel(QtWidgets.QHBoxLayout())
        button_clear = MyPushButtonWithIcon(name="button-clear", text="Clear", icon_type=MyPushButtonIcon.CLEAR)
        button_copy = MyPushButtonWithIcon(name="button-copy", text="Copy", icon_type=MyPushButtonIcon.COPY)
        button_paste = MyPushButtonWithIcon(name="button-paste", text="Paste", icon_type=MyPushButtonIcon.PASTE)

        panel_control.set_style_class("query__control control-panel")
        panel_control.place(button_clear)
        panel_control.place(button_copy)
        panel_control.place(button_paste)
        panel_control.set_spacing(8)
        #button_clear.clicked.connect(lambda: self.get_text_area_content())

        self.place(panel_control)

    def get_query_content(self):
        return self.text_area.toPlainText()