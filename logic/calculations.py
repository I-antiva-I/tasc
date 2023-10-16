from logic.document import Document
from logic.term import Term


# Fill term dictionary with words from document
def fill_terms_via_document(document, index, terms):
    words, counts = Document.modify_words(Document.find_unique_words(Document.extract_words(document.path)))
    for word, count in zip(words, counts):
        if word not in terms:
            terms[word] = Term()
        terms[word].count[index] = count
        document.word_count += count


# Fill term dictionary with words from query
def fill_terms_via_query(query_words, query_index, terms):
    words, counts = Document.modify_words(Document.find_unique_words(query_words))
    for word, count in zip(words, counts):
        if word not in terms:
            terms[word] = Term()
        terms[word].count[query_index] = count
