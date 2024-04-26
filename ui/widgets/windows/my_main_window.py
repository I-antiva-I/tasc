import os
from enum import Enum

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QHBoxLayout

# UI
from ui.widgets.base.my_label import MyLabel
from ui.widgets.base.my_panel import MyPanel
# Logic
from logic.controller import Controller
from logic.calculations import fill_terms_from_query, fill_terms_from_document
from logic.term import Term
from logic.document import Document
from ui.widgets.components.documents.my_documents import MyDocuments
from ui.widgets.components.navigation.my_navigation import MyNavigation
from ui.widgets.components.query.my_query import MyQuery
from ui.widgets.components.results.my_results import MyResults


class SubPanel(Enum):
    DOCUMENTS = 0
    QUERY = 1
    RESULTS = 2
    SETTINGS = 3
    INFORMATION = 4


class MyMainWindow(QtWidgets.QMainWindow):
    def __init__(self, controller: Controller):
        super(MyMainWindow, self).__init__()

        # Window properties
        self.setObjectName("main-window")
        self.setWindowTitle("TF-IDF & COSINE SIMILARITY CALCULATOR")
        self.resize(1000, 500)

        # Central widget
        self.main_panel = MyPanel(layout=QHBoxLayout())
        self.main_panel.set_style_class("main-window__main-panel")
        self.setCentralWidget(self.main_panel)

        # Navigation
        self.navigation = MyNavigation(self.change_active_panel)
        self.main_panel.place(self.navigation)

        # Sub-panels
        self.sub_panels = {
            SubPanel.DOCUMENTS:    MyDocuments(controller=controller, main_widow=self),
            SubPanel.QUERY:        MyQuery(),
            SubPanel.RESULTS:      MyResults(),
            SubPanel.SETTINGS:     MyLabel(text="Settings"),   #TODO
            SubPanel.INFORMATION:  MyLabel(text="Information") #TODO
        }

        # Placement of sub-panels
        for key, panel in self.sub_panels.items():
            panel.hide()
            self.navigation.add_navigation_item(key, key.name)
            self.main_panel.place(panel)

        # Initially active panel (simulating click)
        self.active_panel_key = None
        self.navigation.on_item_clicked(SubPanel.DOCUMENTS)

        # Apply fonts
        path_to_fonts = "./ui/assets/fonts"
        for font_file in os.listdir(path_to_fonts):
            QtGui.QFontDatabase.addApplicationFont(path_to_fonts+'/'+font_file)

        # Apply styles
        path_to_css = "./ui/assets/css/styles.css"
        with open(path_to_css, "r") as file:
            css = file.read()
            self.setStyleSheet(css)

    # Swap currently visible panel
    def change_active_panel(self, new_active_key):
        # Hide previous
        if self.active_panel_key is not None:
            self.sub_panels[self.active_panel_key].hide()

        # Show new
        self.active_panel_key = new_active_key
        self.sub_panels[self.active_panel_key].show()

    #
    def calculate(self):
        print("CALC M")
        self.navigation.on_item_clicked(SubPanel.RESULTS)


        pass

        path_to_css = "./ui/assets/css/styles.css"
        with open(path_to_css, "r") as file:
            css = file.read()
            self.setStyleSheet(css)
        return

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

            data.append([key, terms[key].count, terms[key].tf, terms[key].idf, terms[key].tf_idf])
        #print(data)
        self.sub_panels["results"].update_table(data, number_of_documents, with_query)
        self.change_active_panel("results")
        #df = pandas.DataFrame(data, index=terms.keys())

        #print(df.to_string())
        #print(Term.calculate_cosine_similarity(terms.values()))