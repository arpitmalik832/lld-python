from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum, auto


class DocumentType(Enum):
    TEXT = auto()
    SPREAD_SHEET = auto()


@dataclass
class DocumentParser(ABC):
    path: str

    @abstractmethod
    def parse_document(self):
        pass

    @abstractmethod
    def supports_type(self):
        pass


@dataclass
class DocumentProcessor(ABC):
    document_name: str

    @abstractmethod
    def process_document(self):
        pass

    @abstractmethod
    def supports_type(self):
        pass


@dataclass
class DocumentPrinter(ABC):
    processor: DocumentProcessor

    @abstractmethod
    def print_document(self):
        pass

    @abstractmethod
    def supports_type(self):
        pass


class DocumentFactory(ABC):
    @abstractmethod
    def create_document_parser(self, path: str):
        pass

    @abstractmethod
    def create_document_processor(self, document_name: str):
        pass

    @abstractmethod
    def create_document_printer(self, processor: DocumentProcessor):
        pass

    @abstractmethod
    def supports_format(self) -> DocumentType:
        pass


class TextDocumentFactory(DocumentFactory):
    def create_document_parser(self, path: str):
        return TextDocumentParser(path)

    def create_document_processor(self, document_name: str):
        return TextDocumentProcessor(document_name)

    def create_document_printer(self, processor: DocumentProcessor):
        return TextDocumentPrinter(processor)

    def supports_format(self) -> DocumentType:
        return DocumentType.TEXT


class SpreadsheetDocumentFactory(DocumentFactory):
    def create_document_parser(self, path: str):
        return SpreadsheetDocumentParser(path)

    def create_document_processor(self, document_name: str):
        return SpreadsheetDocumentProcessor(document_name)

    def create_document_printer(self, processor: DocumentProcessor):
        return SpreadsheetDocumentPrinter(processor)

    def supports_format(self) -> DocumentType:
        return DocumentType.SPREAD_SHEET


@dataclass
class SpreadsheetDocumentParser(DocumentParser):
    def parse_document(self):
        # Parse spreadsheet document
        pass

    def supports_type(self):
        return DocumentType.SPREAD_SHEET


@dataclass
class TextDocumentParser(DocumentParser):
    def parse_document(self):
        # Parse text document
        pass

    def supports_type(self):
        return DocumentType.TEXT


@dataclass
class TextDocumentPrinter(DocumentPrinter):
    def print_document(self):
        # Print text document
        print("Printing text document")

    def supports_type(self):
        return DocumentType.TEXT


@dataclass
class SpreadsheetDocumentPrinter(DocumentPrinter):
    def print_document(self):
        # Print spreadsheet document
        print("Printing spreadsheet document")

    def supports_type(self):
        return DocumentType.SPREAD_SHEET


@dataclass
class SpreadsheetDocumentProcessor(DocumentProcessor):
    def process_document(self):
        # Implement spreadsheet document processing logic
        print("Processing a spreadsheet document:", self.document_name)
        # Additional logic for spreadsheet document processing

    def supports_type(self):
        return DocumentType.SPREAD_SHEET

    def perform_data_analysis(self):
        print("Performing data analysis on the spreadsheet.")


@dataclass
class TextDocumentProcessor(DocumentProcessor):
    def process_document(self):
        # Implement text document processing logic
        print("Processing a text document:", self.document_name)
        # Additional logic for text document processing

    def supports_type(self):
        return DocumentType.TEXT
