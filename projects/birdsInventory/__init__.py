from abc import ABC, abstractmethod


class IBird(ABC):
    @abstractmethod
    def walk(self):
        pass


class IFly(ABC):
    @abstractmethod
    def fly(self):
        pass


class Ostrich(IBird):
    def walk(self):
        print("Ostrich is walking")


class Pigeon(IBird, IFly):
    def walk(self):
        print("Pigeon is walking")

    def fly(self):
        print("Pigeon is flying")
