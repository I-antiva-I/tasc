from PyQt5 import QtWidgets

from ui.widgets.base.my_panel import MyPanel
from ui.widgets.base.my_push_button import MyPushButton
from ui.widgets.components.results.my_table_model import MyTableModel


class MyResults(MyPanel):
    def __init__(self):
        super(MyResults, self).__init__(layout=QtWidgets.QVBoxLayout())
        self.table = QtWidgets.QTableView()
        #self.table.horizontalHeader().hide()
        #self.table.verticalHeader().hide()
        self.place(self.table)
        control_panel = MyPanel(layout=QtWidgets.QHBoxLayout())
        button1 = MyPushButton("Export")
        control_panel.place_all(button1)
        self.place(control_panel)

    def update_table(self, data, number_of_documents, with_query):
        # Table data
        number_of_documents = number_of_documents
        with_query = with_query
        number_of_terms = len(data)

        # Span
        self.table.clearSpans()
        column_span = number_of_documents + int(with_query)
        # Term
        self.table.setSpan(0, 0, 2, 1)
        # Counts
        self.table.setSpan(0, 1, 1, column_span)
        # TF
        self.table.setSpan(0, 1+column_span, 1, column_span)
        # IDF
        self.table.setSpan(0, 1+column_span*2, 2, 1)
        # TF-IDF
        self.table.setSpan(0, 2+column_span*2, 1, column_span)
        # Model
        self.table.setModel(MyTableModel(data, number_of_terms, number_of_documents, with_query))


        """
        self.setStretchLastSection(True)
        self.setSortIndicatorShown(True)
        self.setHighlightSections(True)
        self.setSectionsClickable(True)
        self.sectionClicked.connect(lambda: print("HI!"))
        """