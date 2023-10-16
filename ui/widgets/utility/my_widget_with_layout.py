from enum import Enum

from PyQt5 import Qt
from PyQt5.QtWidgets import QWidget, QGridLayout


# Enums
class Alignment(Enum):
    TOP = 1
    BOTTOM = 2
    CENTER = 3


class MyWidgetWithLayout(QWidget):
    def __init__(self):
        super(MyWidgetWithLayout, self).__init__()

    # Add widget to a layout
    def place(self, widget, row=None, col=None, rowSpan=1, colSpan=1):
        # Grid layout
        if type(self.layout()) is QGridLayout:
            if (row is not None) and (col is not None):
                self.layout().addWidget(widget, row, col, rowSpan, colSpan)
            else:
                self.layout().addWidget(widget)
        # VBox/HBox layout
        else:
            self.layout().addWidget(widget)

    # Add multiple widgets to a layout (VBox/HBox)
    def place_all(self, *widgets):
        for widget in widgets:
            self.place(widget)

    # Set margin
    def set_content_margins(self, left=0, top=0, right=0, bottom=0):
        self.layout().setContentsMargins(left, top, right, bottom)

    # Set spacing
    def set_spacing(self, value=0):
        self.layout().setSpacing(value)

    # Set alignment of a layout
    def set_alignment(self, alignment):
        if alignment == Alignment.TOP:
            self.layout().setAlignment(Qt.Qt.AlignTop)
        elif alignment == Alignment.BOTTOM:
            self.layout().setAlignment(Qt.Qt.AlignBottom)
        elif alignment == Alignment.CENTER:
            self.layout().setAlignment(Qt.Qt.AlignCenter)

