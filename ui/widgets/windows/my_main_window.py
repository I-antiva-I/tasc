import os
import pandas

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QHBoxLayout

# UI
from ui.widgets.basic.my_label import MyLabel
from ui.widgets.basic.my_panel import MyPanel
# Logic
from logic.calculations import fill_terms_via_document, fill_terms_via_query
from logic.term import Term
from logic.document import Document
from ui.widgets.documents.my_documents import MyDocuments
from ui.widgets.navigation.my_navigation import MyNavigation
from ui.widgets.query.my_query import MyQuery
from ui.widgets.results.my_results import MyResults


class MyMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()

        # Window properties
        self.setObjectName("main-window")
        self.setWindowTitle("TF-IDF & COSINE SIMILARITY CALCULATOR")
        self.resize(1000, 500)

        # Central widget
        self.main_panel = MyPanel(layout=QHBoxLayout())
        self.main_panel.set_class("main-window__main-panel")
        self.setCentralWidget(self.main_panel)

        # Navigation
        self.navigation = MyNavigation(self.change_active_panel)
        self.main_panel.place(self.navigation)

        # Sub panels
        self.sub_panels = {
            "documents":    MyDocuments(main_window=self),
            "query":        MyQuery(),
            "results":      MyResults(),
            "settings":     MyLabel(text="Settings"),
            "information":  MyLabel(text="Information")
        }
        for key, panel in self.sub_panels.items():
            panel.hide()
            self.navigation.add_navigation_item(key, key.capitalize())
            self.main_panel.place(panel)

        #


        # Active panel
        self.active_panel = self.sub_panels["results"]
        self.active_panel.show()

        # Apply fonts
        path_to_fonts = "./ui/assets/fonts"
        for font_file in os.listdir(path_to_fonts):
            QtGui.QFontDatabase.addApplicationFont(path_to_fonts+'/'+font_file)

        # Apply styles
        path_to_css = "./ui/assets/css/styles.css"
        with open(path_to_css, "r") as file:
            css = file.read()
            self.setStyleSheet(css)

    #
    def change_active_panel(self, key):
        self.active_panel.hide()
        self.active_panel = self.sub_panels[key]
        self.active_panel.show()

    #
    def calculate(self, documents_items):
        print("DOCS", len(documents_items), documents_items)
        print("QUERY", self.sub_panels["query"].get_query_content())

        # Terms and documents
        terms = {}
        documents = []

        included_documents = [item for item in documents_items if item.button_include.isChecked() is True]
        number_of_documents = len(included_documents)

        for document in included_documents:
            documents.append(Document("filename", document.file_path))

        # Settings
        with_query = True
        field_query = self.sub_panels["query"].get_query_content().lower()
        Term.set_term_parameters(number_of_documents, with_query)

        # Fill terms with words from documents
        for index, document in enumerate(documents):
            fill_terms_via_document(document, index, terms)

        # Fill terms with words from query
        if with_query:
            query_words = field_query.split()
            query_index = number_of_documents
            fill_terms_via_query(query_words, query_index, terms)
        data =[]

        for key, term in terms.items():
            # Documents
            for index, document in enumerate(documents):
                term.calculate_tf(index, total_word_count=document.word_count)
                term.calculate_idf()
                term.calculate_tf_idf()
            # Query
            term.calculate_tf(query_index, total_word_count=len(query_words))
            term.calculate_idf()
            term.calculate_tf_idf()

            data.append([terms[key].count, terms[key].tf, terms[key].idf, terms[key].tf_idf])

        df = pandas.DataFrame(data, index=terms.keys())

        print(df.to_string())
        print(Term.calculate_cosine_similarity(terms.values()))