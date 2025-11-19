from abc import ABC, abstractmethod


class Aeroplane(ABC):
    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def land(self):
        pass

    @abstractmethod
    def taxi(self):
        pass
