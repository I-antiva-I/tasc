# Imports
import re
from enum import Enum
import numpy as np


# Enum for word case
class WordCase(Enum):
    UPPER = 1
    LOWER = 2
    SENSITIVE = 3


# Document
class Document:
    def __init__(self, filename: str, filepath: str, is_query: bool = False, is_included: bool = True):
        self.filename: str = filename
        self.filepath: str = filepath
        self.is_query: bool = is_query
        self.is_included: bool = is_included
        self.word_count: int = 0

    @staticmethod
    # Extract words from file and return as array
    def extract_words(path_to_file, word_case=WordCase.LOWER):
        with open(path_to_file, "r") as file:
            if word_case == WordCase.SENSITIVE:
                return np.array(file.read().split())
            elif word_case == WordCase.LOWER:
                return np.array(file.read().lower().split())
            elif word_case == WordCase.UPPER:
                return np.array(file.read().upper().split())

    @staticmethod
    # Remove duplicates from array of words and return unique words with corresponding counts
    def find_unique_words(words):
        unique_words, counts = np.unique(words, return_counts=True)
        return unique_words, counts

    @staticmethod
    # Modify words and corresponding counts via applying patterns
    def modify_words(words_and_counts):
        words, counts = words_and_counts
        patterns = ["(.*?)[?!,.:;]+"]

        for pattern in patterns:
            indexes_to_delete = []
            for index, word in enumerate(words):
                match = re.match(pattern, word)
                if match:
                    clean_word = match.group(1)
                    if clean_word == "":
                        indexes_to_delete.append(index)
                    else:
                        original = np.where(words == clean_word)[0]
                        if len(original):
                            counts[original] +=  counts[index]
                            indexes_to_delete.append(index)
                        else:
                            words[index] = clean_word

            words = np.delete(words, indexes_to_delete)
            counts = np.delete(counts, indexes_to_delete)

        return words, counts
