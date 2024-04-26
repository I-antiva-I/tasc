import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from logic.controller import Controller
from ui.widgets.windows.my_main_window import MyMainWindow


def launch():
    controller = Controller()
    app = QtWidgets.QApplication(sys.argv)
    app.setAttribute(Qt.AA_Use96Dpi)
    main_window = MyMainWindow(controller)
    main_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    launch()
