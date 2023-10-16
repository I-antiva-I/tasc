from PyQt5 import QtWidgets, QtGui
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QPushButton

from ui.widgets.utility.my_widget import MyWidget
from ui.widgets.utility.my_widget_interactive import MyWidgetInteractive


class MyPushButton(QPushButton, MyWidget):
    def __init__(self, text="Default text"):
        super(MyPushButton, self).__init__()

        self.setText(text)

        '''
        # Buttons for file control
        button_add_file =       MyPushButton(text="Add File")
        button_add_folder =     MyPushButton(text="Add Folder")
        button_remove_all =     MyPushButton(text="Remove All")
        button_add_file.clicked.connect(lambda:     self.add_file())
        button_add_folder.clicked.connect(lambda:   self.add_folder())
        button_remove_all.clicked.connect(lambda:   self.remove_all())

        # Button for calculation
        button_calculate = MyPushButton(text="Calculate")
        button_calculate.clicked.connect(lambda: self.calculate())

        # Containers
        panel_file_control =     MyPanel(layout=QtWidgets.QHBoxLayout())
        panel_file_control.place_all(button_add_file, button_add_folder, button_remove_all)
        panel_file_control.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        panel_file_control.set_class("panel--file-control")

        # Placement
        self.group_selected_files = MyGroupFiles()
        self.group_query_field = MyGroupQuery()


        img = MyImage(path_to_image="./ui/assets/images/circle-question-solid.svg")
        self.main_panel.place_all(img, self.group_query_field, self.group_selected_files, panel_file_control, button_calculate)
        '''