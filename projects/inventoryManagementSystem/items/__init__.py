from abc import ABC


class Item(ABC):
    def __init__(self, id: str, name: str, price: float, quantity: int):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_id(self) -> str:
        return self.id

    def get_name(self) -> str:
        return self.name

    def get_price(self) -> float:
        return self.price

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity

    # public int compareTo(Item other) {
    #     return (int) Math.floor(this.price - other.price);
    # }


class Book(Item):
    def __init__(self, id: str, name: str, price: float, quantity: int, author: str):
        super().__init__(id, name, price, quantity)
        self.author = author

    def get_author(self) -> str:
        return self.author


class Clothing(Item):
    def __init__(self, id: str, name: str, price: float, quantity: int, size: str):
        super().__init__(id, name, price, quantity)
        self.size = size

    def get_size(self):
        return self.size


class Electronic(Item):
    def __init__(self, id: str, name: str, price: float, quantity: int, warranty: int):
        super().__init__(id, name, price, quantity)
        self.warranty = warranty

    def get_warranty(self):
        return self.warranty
