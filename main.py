import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from ui.widgets.windows.my_main_window import MyMainWindow


def launch():
    app = QtWidgets.QApplication(sys.argv)
    app.setAttribute(Qt.AA_Use96Dpi)
    main_window = MyMainWindow()
    main_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    launch()


'''
I use PyQt extensively at work. All python code is using python naming
 conventions wherever possible, that is PascalCase for classes,
  and under_score for variables and class members.
   When internal PyQt methods/setters are called or overwritten,
    then PyQt's conventions are used, naturally, but other than that
     I try to stick to pythonic code as much as possible.
'''