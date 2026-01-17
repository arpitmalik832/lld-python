from abc import ABC
from dataclasses import dataclass
from enum import Enum


class DocumentFactory:
    @staticmethod
    def create_document(type, document_name):
        if type == DocumentType.PRESENTATION:
            return PresentationDocumentProcessor(document_name)
        elif type == DocumentType.SPREADSHEET:
            return SpreadsheetDocumentProcessor(document_name)
        elif type == DocumentType.TEXT:
            return TextDocumentProcessor(document_name)
        return None


@dataclass
class DocumentProcessor(ABC):
    def supports_type(self):
        pass

    def process_document(self):
        pass

    def add_slide(self):
        pass


@dataclass
class PresentationDocumentProcessor(DocumentProcessor):
    document_name: str

    def supports_type(self):
        return DocumentType.PRESENTATION

    def process_document(self):
        print(f"Processing a presentation document: {self.document_name}")

    def add_slide(self):
        print("Adding a slide to the presentation.")


@dataclass
class SpreadsheetDocumentProcessor(DocumentProcessor):
    document_name: str

    def supports_type(self):
        return DocumentType.SPREADSHEET

    def process_document(self):
        print(f"Processing a spreadsheet document: {self.document_name}")

    def perform_data_analysis(self):
        print("Performing data analysis on the spreadsheet.")


@dataclass
class TextDocumentProcessor(DocumentProcessor):
    document_name: str

    def supports_type(self):
        return DocumentType.TEXT

    def process_document(self):
        print(f"Processing a text document: {self.document_name}")


class DocumentType(Enum):
    PRESENTATION = "Presentation"
    SPREADSHEET = "Spreadsheet"
    TEXT = "Text"
