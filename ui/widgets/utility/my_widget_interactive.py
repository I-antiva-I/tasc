from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QWidget


class MyWidgetInteractive(QWidget):
    def __init__(self):
        super(MyWidgetInteractive, self).__init__()

        self.on_enter_event = None
        self.on_leave_event = None
        self.on_mouse_click_event = None

    def enterEvent(self, QEvent):
        if callable(self.on_enter_event):
            self.on_enter_event()
        super().enterEvent(QEvent)

    def leaveEvent(self, QEvent):
        super().leaveEvent(QEvent)
        if callable(self.on_leave_event):
            self.on_leave_event()

    def mousePressEvent(self, QEvent):
        super().mousePressEvent(QEvent)

    def mouseReleaseEvent(self, QEvent):
        super().mouseReleaseEvent(QEvent)
        if callable(self.on_mouse_click_event):
            self.on_mouse_click_event()



