from PyQt5 import QtWidgets

from ui.widgets.basic.my_panel import MyPanel
from ui.widgets.results.my_table_model import MyTableModel


class MyResults(MyPanel):
    def __init__(self):
        super(MyResults, self).__init__(layout=QtWidgets.QVBoxLayout())
        self.table = QtWidgets.QTableView()

        # Table data
        number_of_documents = 4
        with_query = True
        number_of_terms = 12

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

        self.table.setModel(MyTableModel(number_of_terms, number_of_documents, with_query))
        self.table.horizontalHeader().hide()
        self.table.verticalHeader().hide()
        self.place(self.table)

        """
        self.setStretchLastSection(True)
        self.setSortIndicatorShown(True)
        self.setHighlightSections(True)
        self.setSectionsClickable(True)
        self.sectionClicked.connect(lambda: print("HI!"))
        """