from abc import ABC
from typing import TypeVar, Generic

T = TypeVar("T")


class Item(ABC):
    next_id: str = "1"

    def __init__(self, name: str, price: float):
        self.id = Item.next_id
        Item.next_id = str(int(Item.next_id) + 1)
        self.name = name
        self.price = price

    def get_id(self) -> str:
        return self.id

    def set_id(self, id: str):
        self.id = id

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str):
        self.name = name

    def get_price(self) -> float:
        return self.price

    def set_price(self, price: float):
        self.price = price


class Item1(Item):
    def __init__(self, name: str, price: float):
        super().__init__(name, price)


class Item2(Item):
    def __init__(self, name: str, price: float):
        super().__init__(name, price)


class Inventory(Generic[T]):
    def __init__(self):
        self.items: list[T] = []


def main():
    item1Inventory = Inventory[Item1]()
    item2Inventory = Inventory[Item2]()


main()
