from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QScrollArea, QVBoxLayout

from ui.widgets.documents.my_documents_control import MyDocumentsControl
from ui.widgets.utility.my_widget_with_layout import Alignment
from ui.widgets.documents.my_documents_item import MyDocumentsItem
from ui.widgets.basic.my_label import MyLabel
from ui.widgets.basic.my_panel import MyPanel


class MyDocuments(MyPanel):
    def __init__(self, main_window):
        super(MyDocuments, self).__init__(layout=QVBoxLayout())

        # Data
        self.documents_items = []
        self.query_index = -1

        # Header
        label_file_index =      MyLabel(text="Index")
        label_file_name =       MyLabel(text="File name")
        label_controls =        MyLabel(text="Controls")
        self.panel_header =     MyPanel(layout=QtWidgets.QGridLayout())

        self.panel_header.place(label_file_index, 0, 0, colSpan=1)
        self.panel_header.place(label_file_name, 0, 1, colSpan=6)
        self.panel_header.place(label_controls, 0, 1+6, colSpan=5)

        label_file_name.set_class("label--file-name")
        label_file_index.set_class("label--file-index")
        label_controls.set_class("label--file-controls")
        self.panel_header.set_class("documents__header")

        # Info panel (no files)
        self.label_no_items = MyLabel(text="No files selected")
        self.label_no_items.set_class("documents__info")

        # Content panel
        self.content_panel = MyPanel(layout=QtWidgets.QVBoxLayout())
        self.content_panel.set_alignment(Alignment.TOP)
        self.content_panel.set_spacing(4)

        scroll_area = QScrollArea()
        scroll_area.setWidget(self.content_panel)
        scroll_area.setWidgetResizable(True)
        self.scroll_bar = scroll_area.verticalScrollBar()
        self.scroll_bar.rangeChanged.connect(lambda: self.r())

        # Control panel
        control_panel = MyDocumentsControl(widget_documents=self, main_window=main_window)

        # Main panel
        main_panel = MyPanel(layout=QtWidgets.QVBoxLayout())
        main_panel.place(self.panel_header)
        main_panel.place(self.label_no_items)
        main_panel.place(scroll_area)
        main_panel.place(control_panel)
        self.place(main_panel)


    def r(self):
        return
        if self.scroll_bar.maximum() == 0:
            self.panel_header.toggle_class("group-files__header--with-scroll", False)
        else:
            self.panel_header.toggle_class("group-files__header--with-scroll", True)
        print(self.panel_header.class_list)
        print("~", self.scroll_bar.value(), self.scroll_bar.maximum())
        self.setStyleSheet("")

    def update_target(self, index, isChecked):
        if isChecked:
            if self.query_index != -1:
                self.documents_items[self.query_index].button_query.setChecked(False)
            self.query_index = index
        else:
            self.query_index = -1

    def add_item(self, path, name):
        if self.label_no_items.isVisible():
            self.label_no_items.hide()
        item = MyDocumentsItem(widget_documents=self, index=len(self.documents_items), text=name, path=path)
        self.documents_items.append(item)
        self.content_panel.place(item)
        if self.query_index == -1:
            self.query_index = 0
            item.button_query.setChecked(True)

    def remove_item(self, index):
        for item in self.documents_items[index+1:]:
            item.update_index()

        self.documents_items.pop(index)
        if index == self.query_index:
            self.query_index = -1
        else:
            self.query_index = max(self.query_index - 1, -1)

        if len(self.documents_items) == 0:
            self.label_no_items.show()

    def remove_all(self):
        for item in self.documents_items:
            item.deleteLater()
        self.documents_items.clear()
        self.label_no_items.show()
