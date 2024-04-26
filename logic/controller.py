from typing import List

from logic.document import Document


class Controller:
    def __init__(self):
        self.documents: List[Document] = []
        self.query_index: int = -1
        self.use_query_field: bool = False

    def toggle_use_query_field(self) -> None:
        self.use_query_field = not self.use_query_field

    def remove_document(self, index: int) -> None:
        self.documents.pop(index)

    def append_document(self, document: Document) -> None:
        self.documents.append(document)

    def set_document_filename(self, index: int, filename: str) -> None:
        self.documents[index].filename = filename

    def set_document_filepath(self, index: int, filepath: str) -> None:
        self.documents[index].filepath = filepath

    def set_document_query(self, index: int, is_query: bool) -> None:
        self.documents[index].is_query = is_query

    def set_document_included(self, index: int, is_included: bool) -> None:
        self.documents[index].is_included = is_included

