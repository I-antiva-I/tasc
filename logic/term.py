import cmath
import numpy as np
from enum import Enum


# Enum for idf notation
class IDFNotation(Enum):
    SCIKIT_LEARN = 1
    STANDARD = 2


# Enum for method of term frequency calculation
class TFMethod(Enum):
    RAW_COUNT = 1
    TOTAL_COUNT = 2
    MAX_COUNT = 3
    LOG_SCALED = 4
    BOOLEAN = 5


# Term
class Term:
    # Class parameters
    with_query = False
    number_of_documents = 0

    def __init__(self):
        self.count = np.zeros(Term.number_of_documents+int(Term.with_query))
        self.tf = np.zeros(Term.number_of_documents+int(Term.with_query))
        self.idf = 0
        self.tf_idf = np.zeros(Term.number_of_documents+int(Term.with_query))

    @classmethod
    # Set class parameters
    def set_term_parameters(cls, number_of_documents=0, with_query=False):
        cls.number_of_documents = number_of_documents
        cls.with_query = with_query

    # Find number of zeros in counts
    def number_of_documents_with_term(self):
        return len(np.where(self.count[:Term.number_of_documents] != 0)[0])

    # Term Frequency (TF)
    def calculate_tf(self, document_index, total_word_count=1, max_word_count=1,
                     precision=5, base=10, method=TFMethod.TOTAL_COUNT):
        # Safe
        max_word_count = max(max_word_count, 1)
        total_word_count = max(total_word_count, 1)

        # Method #1: Raw word count
        if method == TFMethod.RAW_COUNT:
            self.tf[document_index] = self.count[document_index]

        # Method #2: Normalization with total word count
        elif method == TFMethod.TOTAL_COUNT:
            self.tf[document_index] = round(self.count[document_index] / total_word_count, precision)

        # Method #3: Normalization with max word count
        elif method == TFMethod.MAX_COUNT:
            self.tf[document_index] = round(self.count[document_index]  / max_word_count, precision)

        # Method #4: Logarithmically scaled
        elif method == TFMethod.LOG_SCALED:
            result = cmath.log(1+self.count[document_index] , base)
            self.tf[document_index] = round(result.real, precision)

        # Method #5: Boolean
        elif method == TFMethod.BOOLEAN:
            self.tf[document_index] = int(self.count[document_index]  > 0)

    # Inverse Document Frequency (IDF)
    def calculate_idf(self, precision=5, base=10, notation=IDFNotation.SCIKIT_LEARN):
        documents = Term.number_of_documents
        documents_with_term = self.number_of_documents_with_term()

        # Scikit-Learn notation
        if notation == IDFNotation.SCIKIT_LEARN:
            result = cmath.log((documents+1) / (documents_with_term+1), base)
            self.idf =  round(result.real + 1, precision)

        # Standard notation
        elif notation == IDFNotation.STANDARD:
            if (documents != 0) and (documents_with_term != 0):
                result = cmath.log(documents / documents_with_term, base)
                self.idf = round(result.real, precision)

    # Term Frequency * Inverse Document Frequency (TF-IDF)
    def calculate_tf_idf(self, precision=5):
        self.tf_idf = np.round(np.multiply(self.tf, self.idf), precision)

    @staticmethod
    # Cosine similarity between query and other documents
    def calculate_cosine_similarity(terms, precision=5):
        query_index = Term.number_of_documents
        similarity = np.zeros(Term.number_of_documents)
        for index in range(Term.number_of_documents):
            numerator = sum(map(lambda term: term.tf_idf[index] * term.tf_idf[query_index], terms))
            denominator = (sum(map(lambda term: term.tf_idf[index]**2, terms))**0.5) * \
                          (sum(map(lambda term: term.tf_idf[query_index]**2, terms))**0.5)

            similarity[index] = round(numerator / denominator, precision) if denominator != 0 else 0

        return similarity


