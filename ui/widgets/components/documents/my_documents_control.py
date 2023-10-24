import os

from PyQt5.QtWidgets import QGridLayout, QFileDialog

from ui.widgets.base.my_panel import MyPanel
from ui.widgets.base.my_push_button_with_icon import MyPushButtonWithIcon, MyPushButtonIcon


class MyDocumentsControl(MyPanel):
    def __init__(self, widget_documents, main_window):
        super(MyDocumentsControl, self).__init__(layout=QGridLayout())

        # File control
        button_add_file =       MyPushButtonWithIcon(name="button-add-file", text="Add File", icon_type=MyPushButtonIcon.FILE)
        button_add_folder =     MyPushButtonWithIcon(name="button-add-folder", text="Add Folder", icon_type=MyPushButtonIcon.FOLDER)
        button_remove_all =     MyPushButtonWithIcon(name="button-remove-all", text="Remove All", icon_type=MyPushButtonIcon.REMOVE)
        button_add_file.clicked.connect(lambda:     self.add_file())
        button_add_folder.clicked.connect(lambda:   self.add_folder())
        button_remove_all.clicked.connect(lambda:   self.remove_all())

        # Calculation
        button_calculate = MyPushButtonWithIcon(name="button-calculate", text="Calculate", icon_type=MyPushButtonIcon.CALCULATE)
        button_calculate.clicked.connect(lambda: main_window.calculate(widget_documents.documents_items))

        self.place(button_remove_all, row=0, col=0)
        self.place(button_add_folder, row=0, col=1)
        self.place(button_add_file, row=0, col=2)
        self.place(button_calculate, row=1, col=0, colSpan=1)

        self.set_spacing(4)
        self.set_class("documents__control control-panel")

        self.widget_documents = widget_documents

    # Add directory
    def add_folder(self):
        # Prepare file dialog
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.FileMode.Directory)
        dialog.setViewMode(QFileDialog.ViewMode.Detail)

        # Open file dialog
        if dialog.exec():
            path = dialog.selectedFiles()[0]
        else:
            return

        # Add files from directory
        if os.path.isdir(path):
            for file in os.listdir(path):
                name, extension = os.path.splitext(file)
                if extension == ".txt":
                    self.widget_documents.add_item(name=name + extension, path=path + "/" + name + extension)

    # Add file
    def add_file(self):
        # Prepare file dialog
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        dialog.setNameFilter("TXT (*.txt);;All (*)")
        dialog.setViewMode(QFileDialog.ViewMode.Detail)

        # Open file dialog
        if dialog.exec():
            paths = dialog.selectedFiles()
        else:
            return

        # Add selected paths
        for path in paths:
            if os.path.isfile(path):
                name, extension = os.path.splitext(path)
                if extension == ".txt":
                    self.widget_documents.add_item(name=os.path.basename(name + extension), path=path)

    #
    def remove_all(self):
        self.widget_documents.remove_all()