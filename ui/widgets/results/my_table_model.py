from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QModelIndex
from PyQt5.QtCore import QAbstractTableModel


class MyTableModel(QAbstractTableModel):
    def __init__(self, number_of_terms=12, number_of_documents=4, with_query=True,):
        super(MyTableModel, self).__init__()
        self.data = []

        # counts*d + tf*d + tf-idf*d idf +
        number_of_rows = number_of_terms+2
        number_of_columns = (number_of_documents+int(with_query))*3+2

        for row in range(number_of_rows):
            self.data.append([])
            for column in range(number_of_columns):
                self.data[row].append("?")

        self.data[0][0] = "Term"

    def p(self, header, start, end, with_query):

        self.data[0][start] = header

        for i in range(start, end):
            self.data[1][i+1] = "D"+str(i+1)

        #if with_query:

        '''
    
        for i in range(number_of_documents):
            self.data[0][i+1] = "TF"
            self.data[1][i+1] = "D"+str(i+1)
        if with_query:
            self.data[0][number_of_documents+1] = "TF"
            self.data[1][number_of_documents+1] = "Q"

        self.data[0][number_of_documents+2] = "IDF"
        self.data[1][number_of_documents+2] = "IDF"

        for i in range(number_of_documents):
            self.data[0][i+1+number_of_documents+2] = "TF-IDF"
            self.data[1][i+1+number_of_documents+2] = "D"+str(i+1)
        if with_query:
            self.data[0][number_of_documents+1+number_of_documents+2] = "TF-IDF"
            self.data[1][number_of_documents+1+number_of_documents+2] = "Q"
        '''

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