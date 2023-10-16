import os

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QRadioButton, QCheckBox, QSizePolicy

from ui.widgets.basic.my_label import MyLabel
from ui.widgets.basic.my_panel import MyPanel
from ui.widgets.basic.my_push_button import MyPushButton


class MyDocumentsItem(MyPanel):
    def __init__(self, widget_documents, index=None, text=None, path=None):
        super(MyDocumentsItem, self).__init__(layout=QtWidgets.QGridLayout())

        # Data
        self.file_index = index
        self.file_path = path
        self.is_query = False
        self.is_included = True
        self.widget_documents = widget_documents

        # Labels
        self.label_file_index = MyLabel(text=str(index + 1))
        self.label_file_name = MyLabel(text=str(text))

        self.label_file_index.set_class("label--file-index")
        self.label_file_name.set_class("label--file-name")
        self.label_file_name.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)

        # Buttons
        self.button_query =         QRadioButton(text="Query")
        self.button_include =       QCheckBox(text="Included")
        button_remove =             MyPushButton(text="Remove")
        button_edit_path =          MyPushButton(text="Edit")

        self.button_query.clicked.connect(self.on_query_clicked)
        self.button_include.setChecked(self.is_included)
        self.button_include.clicked.connect(self.on_include_clicked)
        button_remove.clicked.connect(self.on_remove_clicked)
        button_edit_path.clicked.connect(self.on_edit_clicked)

        # Control panel
        control_panel = MyPanel(layout=QtWidgets.QHBoxLayout())
        control_panel.place_all(self.button_query, self.button_include, button_remove, button_edit_path)

        # Placement
        self.place(self.label_file_index, 0, 0, colSpan=1)
        self.place(self.label_file_name, 0, 1, colSpan=6)
        self.place(control_panel, 0, 1+6, colSpan=5)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        class_modifier = "--even" if (index % 2 == 0) else "--odd"
        self.set_class("documents__item documents__item"+class_modifier)

    # Remove button
    def on_remove_clicked(self):
        self.widget_documents.remove_item(self.file_index)
        self.deleteLater()

    # Include button
    def on_include_clicked(self):
        self.is_included = not self.is_included

    # Query button
    def on_query_clicked(self):
        self.is_query = not self.is_query
        self.widget_documents.update_target(self.file_index, self.is_query)

    # Edit button
    def on_edit_clicked(self):
        # Prepare file dialog
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        dialog.setNameFilter("TXT (*.txt);;All (*)")
        dialog.setViewMode(QFileDialog.ViewMode.Detail)

        # Open file dialog
        if dialog.exec():
            dialog_path = dialog.selectedFiles()[0]
        else:
            return

        # Check if file is valid
        if os.path.isfile(dialog_path):
            name, extension = os.path.splitext(dialog_path)
            if extension == ".txt":
                self.update_file_data(dialog_path, os.path.basename(name + extension))

    # Update file name label and file path
    def update_file_data(self, path, name):
        self.file_path = path
        self.label_file_name.setText(name)

    # Update index and style
    def update_index(self):
        self.file_index = self.file_index - 1
        self.label_file_index.setText(str(self.file_index + 1))

        new_modifier = "--even" if (self.file_index % 2 == 0) else "--odd"
        old_modifier = "--odd" if (self.file_index % 2 == 0) else "--even"

        self.toggle_class("documents__item"+old_modifier, with_reset=False)
        self.toggle_class("documents__item"+new_modifier)

