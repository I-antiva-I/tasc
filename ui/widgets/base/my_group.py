from PyQt5 import QtWidgets

from ui.widgets.utility.my_widget import MyWidget
from ui.widgets.utility.my_widget_with_layout import MyWidgetWithLayout


class MyGroup(QtWidgets.QGroupBox, MyWidget, MyWidgetWithLayout):
    def __init__(self, layout=QtWidgets.QVBoxLayout(), title="Default title"):
        super(MyGroup, self).__init__()

        self.setLayout(layout)
        self.setTitle(title)

        self.set_spacing(0)
        self.set_content_margins(0)
