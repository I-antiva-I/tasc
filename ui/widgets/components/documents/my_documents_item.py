import os

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QRadioButton, QCheckBox, QSizePolicy

from logic.controller import Controller
from logic.document import Document
from ui.widgets.base.my_label import MyLabel
from ui.widgets.base.my_panel import MyPanel
from ui.widgets.base.my_push_button import MyPushButton
from ui.widgets.base.my_push_button_with_icon import MyPushButtonWithIcon
from ui.widgets.components.documents import my_documents as comp_docs


class MyDocumentsItem(MyPanel):
    def __init__(self, my_documents: "comp_docs.MyDocuments", controller: Controller, index: int, filename: str):
        super(MyDocumentsItem, self).__init__(layout=QtWidgets.QGridLayout())

        # References
        self.my_documents = my_documents
        self.controller = controller

        # Index
        self.document_index = index

        # Style class
        class_modifier = "--even" if (index % 2 == 0) else "--odd"
        self.set_style_class("documents__item documents__item" + class_modifier)

        # Labels
        self.label_index =      MyLabel(text=str(index+1))
        self.label_filename =   MyLabel(text=str(filename))
        self.label_index.set_style_class("label--index")
        self.label_filename.set_style_class("label--filename")
        self.label_filename.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)

        # Buttons
        self.button_query =         QRadioButton(text="Query")
        self.button_include =       QCheckBox(text="Included")
        button_remove =             MyPushButton(text="Remove")
        button_edit_path =          MyPushButton(text="Edit")
        self.button_include.setChecked(True)

        # Connect
        self.button_query.clicked.connect(self.on_query_clicked)
        self.button_include.clicked.connect(self.on_include_clicked)
        button_remove.clicked.connect(self.on_remove_clicked)
        button_edit_path.clicked.connect(self.on_edit_clicked)

        # Control panel
        panel_control = MyPanel(layout=QtWidgets.QHBoxLayout())
        panel_control.place_all(self.button_query, self.button_include, button_remove, button_edit_path)

        # Placement
        self.place(self.label_index, 0, 0, colSpan=1)
        self.place(self.label_filename, 0, 1, colSpan=6)
        self.place(panel_control, 0, 1+6, colSpan=5)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.set_spacing(8)

    # Remove button clicked
    def on_remove_clicked(self):
        self.my_documents.remove_document(self.document_index)

    # Include check box clicked
    def on_include_clicked(self):
        self.my_documents.update_document(self.document_index, is_included=self.button_include.isChecked())

    # Query radio box clicked
    def on_query_clicked(self):
        self.my_documents.update_document(self.document_index, is_query=self.button_query.isChecked())

    # Edit button clicked
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
                self.my_documents.update_document(index=self.document_index,
                                                  filename=os.path.basename(name + extension),
                                                  filepath=dialog_path)

    # Lower index of document, change label text and restyle self
    def lower_index(self):
        self.document_index = self.document_index-1

        self.label_index.setText(str(self.document_index + 1))

        new_modifier = "--even" if (self.document_index % 2 == 0) else "--odd"
        old_modifier = "--odd" if (self.document_index  % 2 == 0) else "--even"

        self.toggle_style_class("documents__item" + old_modifier, with_reset=False)
        self.toggle_style_class("documents__item" + new_modifier)

