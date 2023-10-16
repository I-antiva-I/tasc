from PyQt5 import QtWidgets

from ui.widgets.utility.my_widget import MyWidget
from ui.widgets.utility.my_widget_with_layout import MyWidgetWithLayout


class MyPanel(QtWidgets.QFrame, MyWidget, MyWidgetWithLayout):
    def __init__(self, layout=QtWidgets.QVBoxLayout()):
        super(MyPanel, self).__init__()

        self.setLayout(layout)

        self.set_spacing(0)
        self.set_content_margins(0)
