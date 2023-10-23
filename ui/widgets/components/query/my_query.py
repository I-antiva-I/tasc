from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPlainTextEdit

from ui.widgets.base.my_group import MyGroup
from ui.widgets.base.my_panel import MyPanel
from ui.widgets.base.my_push_button import MyPushButtonWithIcon, MyPushButtonIcon


class MyQuery(MyPanel):
    def __init__(self):
        super(MyQuery, self).__init__(layout=QtWidgets.QVBoxLayout())

        self.text_area = QPlainTextEdit()
        self.place(self.text_area)

        # Query control
        control_panel = MyPanel(QtWidgets.QHBoxLayout())
        button_clear = MyPushButtonWithIcon(name="button-clear", text="Clear", icon_type=MyPushButtonIcon.CLEAR)
        button_copy = MyPushButtonWithIcon(name="button-copy", text="Copy", icon_type=MyPushButtonIcon.COPY)
        button_paste = MyPushButtonWithIcon(name="button-paste", text="Paste", icon_type=MyPushButtonIcon.PASTE)

        control_panel.place(button_clear)
        control_panel.place(button_copy)
        control_panel.place(button_paste)
        #button_clear.clicked.connect(lambda: self.get_text_area_content())

        self.place(control_panel)

    def get_query_content(self):
        return self.text_area.toPlainText()