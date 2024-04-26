from typing import Dict

from logic.document import Document
from logic.term import Term


# Fill term dictionary with words from document
def fill_terms_from_document(document: Document, index: int, terms: Dict[str, Term]):
    words, counts = Document.modify_words(Document.find_unique_words(Document.extract_words(document.filepath)))
    for word, count in zip(words, counts):
        if word not in terms:
            terms[word] = Term()
        terms[word].count[index] = count
        document.word_count += count


# Fill term dictionary with words from query field
def fill_terms_from_query(query: str, query_index:int, terms: Dict[str, Term]):
    words, counts = Document.modify_words(Document.find_unique_words(query))
    for word, count in zip(words, counts):
        if word not in terms:
            terms[word] = Term()
        terms[word].count[query_index] = count
