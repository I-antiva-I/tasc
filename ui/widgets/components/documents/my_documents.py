from typing import List

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QScrollArea, QVBoxLayout

from logic.controller import Controller
from logic.document import Document
from ui.widgets.components.documents.my_documents_control import MyDocumentsControl
from ui.widgets.utility.my_widget_with_layout import Alignment
from ui.widgets.components.documents.my_documents_item import MyDocumentsItem
from ui.widgets.base.my_label import MyLabel
from ui.widgets.base.my_panel import MyPanel
from ui.widgets.windows import my_main_window as wins_my_main


class MyDocuments(MyPanel):
    def __init__(self, controller: Controller, main_widow: "wins_my_main.MyMainWindow"):
        super(MyDocuments, self).__init__(layout=QVBoxLayout())

        self.controller = controller
        self.main_widow = main_widow
        self.set_style_class("documents")

        # All child nodes that represent documents
        self.documents_items :  List[MyDocumentsItem] = []

        # Index of query document
        self.query_index = -1

        # Header
        self.panel_header =     MyPanel(layout=QtWidgets.QGridLayout())

        # Header labels
        label_file_index =      MyLabel(text="Index")
        label_filename =        MyLabel(text="Filename")
        label_controls =        MyLabel(text="Controls")

        # Placement of header labels
        self.panel_header.place(label_file_index, 0, 0, colSpan=1)
        self.panel_header.place(label_filename, 0, 1, colSpan=4)
        self.panel_header.place(label_controls, 0, 1+4, colSpan=7)
        self.panel_header.set_spacing(8)

        # Classes for header
        label_filename.set_style_class("documents__label label--filename")
        label_file_index.set_style_class("documents__label label--file-index")
        label_controls.set_style_class("documents__label label--file-controls")
        self.panel_header.set_style_class("documents__header")

        # Content panel
        self.panel_content = MyPanel(layout=QtWidgets.QVBoxLayout())
        self.panel_content.set_style_class("documents__content")
        self.panel_content.set_alignment(Alignment.TOP)
        self.panel_content.set_spacing(8)

        # Scroll area for content panel
        scroll_area = QScrollArea()
        scroll_area.setWidget(self.panel_content)
        scroll_area.setWidgetResizable(True)
        self.scroll_bar = scroll_area.verticalScrollBar()
        self.scroll_bar.rangeChanged.connect(lambda: self.scroll_bar_gap())

        # Control panel
        panel_control = MyDocumentsControl(my_documents=self)

        # Placement
        self.place_all(self.panel_header, scroll_area, panel_control)

    # Add document
    def add_document(self, filepath, filename):
        self.controller.append_document(Document(filename=filename, filepath=filepath))

        index = len(self.documents_items)
        item = MyDocumentsItem(my_documents=self, controller=self.controller, index=index, filename=filename)
        self.documents_items.append(item)

        # Place new item
        self.panel_content.place(item)

        # If no query selected, then select first
        if self.query_index == -1:
            item.button_query.setChecked(True)
            item.on_query_clicked()

        print(self.controller.documents[0].is_query)

    # Update document
    def update_document(self, index: int , is_included: bool = None, is_query: bool = None,
                        filepath: str = None, filename: str = None):

        if is_included is not None:
            self.controller.set_document_included(index, is_included)

        if filepath is not None:
            self.controller.set_document_filepath(index, filepath)

        if filename is not None:
            self.controller.set_document_filename(index, filename)
            self.documents_items[self.query_index].label_filename.setText(filename)

        if is_query is not None:
            if is_query is True:
                if self.query_index != -1:
                    self.documents_items[self.query_index].button_query.setChecked(False)
                    self.controller.set_document_query(self.query_index, False)
                self.query_index = index
            else:
                self.query_index = -1
            self.controller.set_document_query(index, is_query)

        print(index, is_included, is_query, filepath, filename)

    # Remove document at index
    def remove_document(self, index: int):
        # Lower larger indexes
        for item in self.documents_items[index+1:]:
            item.lower_index()

        self.documents_items.pop(index).deleteLater()
        self.controller.remove_document(index)

        if index == self.query_index:
            self.query_index = -1

    # Add/Remove addition gap if scroll bar is shown
    def scroll_bar_gap(self):
        if self.scroll_bar.maximum() == 0:
            self.panel_header.toggle_style_class("documents__header--with-scroll", False)
        else:
            self.panel_header.toggle_style_class("documents__header--with-scroll", True)

    # Remove all documents
    def remove_all(self):
        # Remove UI
        for item in self.documents_items:
            item.deleteLater()
        # Remove data
        self.documents_items.clear()
        self.controller.documents.clear()

    #
    def calculate(self):
        self.main_widow.calculate()