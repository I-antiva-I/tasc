from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QModelIndex
from PyQt5.QtCore import QAbstractTableModel


class MyTableModel(QAbstractTableModel):
    def __init__(self, data, number_of_terms, number_of_documents, with_query):
        super(MyTableModel, self).__init__()
        self.data = []

        # counts*d + tf*d + tf-idf*d idf +
        number_of_rows = number_of_terms+2
        number_of_columns = (number_of_documents+int(with_query))*3+2

        # Fill in placeholder data
        for row in range(number_of_rows):
            self.data.append([])
            for column in range(number_of_columns):
                self.data[row].append("?")
        # Headers
        self.insert_headers("Term",      0, -1, False)
        self.insert_headers("Counts",    1, number_of_documents, with_query)
        self.insert_headers("TF",        number_of_documents+int(with_query)+1, number_of_documents, with_query)
        self.insert_headers("IDF",       (number_of_documents+int(with_query))*2+1, -1, False)
        self.insert_headers("TF-IDF",    (number_of_documents+int(with_query))*2+2, number_of_documents, with_query)

        # Data
        self.insert_data(data)

    def insert_headers(self, header, starting_index, document_count, with_query):
        self.data[0][starting_index] = header
        for i in range(document_count):
            self.data[1][i+starting_index] = "D"+str(i+1)
        if with_query:
            self.data[1][starting_index+document_count] = "Q"

    def insert_data(self, data):
        for term in range(len(data)):
            self.data[term+2][0] = data[term][0]
            offset = 1

            for counts in (data[term][1]):
                self.data[term + 2][offset] = counts
                offset += 1

            for tf in (data[term][2]):
                self.data[term+2][offset] = tf
                offset += 1

            self.data[term + 2][offset] = data[term][3]
            offset += 1

            for tf_idf in (data[term][4]):
                self.data[term+2][offset] = tf_idf
                offset += 1

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self.data)

    def columnCount(self, parent=QtCore.QModelIndex()):
        return len(self.data[0])

    def data(self, index: QModelIndex, role: int):
        if role == Qt.DisplayRole:
            row = index.row()
            col = index.column()
            return str(self.data[row][col])
        elif role == Qt.TextAlignmentRole:
            if index.row() <= 1:
                return Qt.AlignCenter