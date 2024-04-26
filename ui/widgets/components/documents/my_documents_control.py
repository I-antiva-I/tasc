import os

from PyQt5.QtWidgets import QGridLayout, QFileDialog

from ui.widgets.base.my_panel import MyPanel
from ui.widgets.base.my_push_button_with_icon import MyPushButtonWithIcon, MyPushButtonIcon
from ui.widgets.components.documents import my_documents as comp_my_docs


class MyDocumentsControl(MyPanel):
    def __init__(self, my_documents: "comp_my_docs.MyDocuments"):
        super(MyDocumentsControl, self).__init__(layout=QGridLayout())

        # File control buttons
        button_add_file =       MyPushButtonWithIcon(name="button-add-file", text="Add File", icon_type=MyPushButtonIcon.FILE)
        button_add_folder =     MyPushButtonWithIcon(name="button-add-folder", text="Add Folder", icon_type=MyPushButtonIcon.FOLDER)
        button_remove_all =     MyPushButtonWithIcon(name="button-remove-all", text="Remove All", icon_type=MyPushButtonIcon.REMOVE)
        button_add_file.clicked.connect(lambda:     self.add_file())
        button_add_folder.clicked.connect(lambda:   self.add_folder())
        button_remove_all.clicked.connect(lambda:   self.remove_all())
        # Calculate button
        button_calculate = MyPushButtonWithIcon(name="button-calculate", text="Calculate", icon_type=MyPushButtonIcon.CALCULATE)
        button_calculate.clicked.connect(lambda: my_documents.calculate())

        # Placement
        self.place(button_remove_all, row=0, col=0)
        self.place(button_add_folder, row=0, col=1)
        self.place(button_add_file, row=0, col=2)
        self.place(button_calculate, row=1, col=0, colSpan=1)
        self.set_spacing(8)
        self.set_style_class("documents__control control-panel")

        # Reference to MyDocuments widget
        self.my_documents = my_documents

    # Remove all documents
    def remove_all(self):
        self.my_documents.remove_all()

    # Add directory
    def add_folder(self):
        # Prepare file dialog
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.FileMode.Directory)
        dialog.setViewMode(QFileDialog.ViewMode.Detail)
        # Start file dialog
        if dialog.exec():
            path = dialog.selectedFiles()[0]
        else:
            return

        # Add files from directory
        if os.path.isdir(path):
            for file in os.listdir(path):
                name, extension = os.path.splitext(file)
                if extension == ".txt":
                    self.my_documents.add_document(filename=os.path.basename(name + extension), filepath=path+"/"+name+extension)

    # Add a single file to the document corpus
    def add_file(self):
        # Prepare file dialog
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        dialog.setNameFilter("TXT (*.txt);;All (*)")
        dialog.setViewMode(QFileDialog.ViewMode.Detail)

        # Start file dialog
        if dialog.exec():
            paths = dialog.selectedFiles()
        else:
            return

        # Add selected paths
        for path in paths:
            if os.path.isfile(path):
                name, extension = os.path.splitext(path)
                if extension == ".txt":
                    self.my_documents.add_document(filename=os.path.basename(name + extension), filepath=path)

