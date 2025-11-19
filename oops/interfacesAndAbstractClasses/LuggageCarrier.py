from abc import ABC, abstractmethod


class LuggageCarrier(ABC):
    @abstractmethod
    def carry_luggage(self):
        pass
