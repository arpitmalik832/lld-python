from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List


@dataclass
class GoogleTranslationRequest:
    text: str
    source_language: str
    target_language: str
    confidence_threshold: float


class GoogleTranslateApi:
    def convert(self, request: GoogleTranslationRequest) -> str:
        return "Translated text"

    def get_languages(self) -> List[str]:
        return ["hindi", "marathi", "kannada"]


class MicrosoftTranslateApi:
    def translate(self, text: str, source_language: str, target_language: str) -> str:
        return "Translated text"

    def get_supported_languages(self) -> List[str]:
        return ["hindi", "marathi", "kannada"]


@dataclass
class TranslationRequest:
    text: str
    source_language: str
    target_language: str
    confidence_threshold: float


class TranslationAdapter(ABC):
    @abstractmethod
    def translate(self, request: TranslationRequest) -> str:
        pass

    @abstractmethod
    def get_supported_languages(self) -> List[str]:
        pass


class MicrosoftTranslationAdapter(TranslationAdapter):
    def __init__(self):
        self.microsoft_translate_api = MicrosoftTranslateApi()

    def translate(self, request: GoogleTranslationRequest) -> str:
        return self.microsoft_translate_api.translate(
            request.text, request.source_language, request.target_language
        )

    def get_supported_languages(self) -> List[str]:
        return self.microsoft_translate_api.get_supported_languages()


class GoogleTranslationAdapter(TranslationAdapter):
    def __init__(self):
        self.google_translate_api = GoogleTranslateApi()

    def translate(self, request: TranslationRequest) -> str:
        return self.google_translate_api.convert(
            GoogleTranslationRequest(
                request.text,
                request.source_language,
                request.target_language,
                request.confidence_threshold,
            )
        )

    def get_supported_languages(self) -> List[str]:
        return self.google_translate_api.get_languages()
