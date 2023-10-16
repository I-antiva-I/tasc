from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPlainTextEdit

from ui.widgets.basic.my_group import MyGroup
from ui.widgets.basic.my_panel import MyPanel
from ui.widgets.basic.my_push_button import MyPushButton


class MyQuery(MyPanel):
    def __init__(self):
        super(MyQuery, self).__init__(layout=QtWidgets.QVBoxLayout())

        self.text_area = QPlainTextEdit()
        self.place(self.text_area)

        # Query control
        control_panel = MyPanel(QtWidgets.QHBoxLayout())
        button_clear = MyPushButton(text="Clear")
        button_copy = MyPushButton(text="Copy")
        button_paste = MyPushButton(text="Paste")

        control_panel.place(button_clear)
        control_panel.place(button_copy)
        control_panel.place(button_paste)
        #button_clear.clicked.connect(lambda: self.get_text_area_content())

        self.place(control_panel)

    def get_query_content(self):
        return self.text_area.toPlainText()