from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, amt: float):
        pass


class PremiumDiscount(DiscountStrategy):
    def apply(self, amt: float):
        return amt - amt * 0.5


class StandardDiscount(DiscountStrategy):
    def apply(self, amt: float):
        return amt - amt * 0.2


class Item:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price


class Order:
    def __init__(self, items: list[Item], total_amt):
        self.__items = items
        self.__total_amt = total_amt

    def get_items(self):
        return self.__items

    def add_item(self, item):
        self.__items.append(item)

    def remove_item(self, item):
        self.__items.remove(item)

    def get_total_amt(self):
        return self.__total_amt

    def set_total_amt(self, total_amt):
        self.__total_amt = total_amt


class OrderProcessor:
    def is_order_valid(self, order: Order):
        return not len(order.get_items()) == 0 and order.get_total_amt() > 0

    def calculate_order_price(self, order: Order):
        amt = 0

        for i in order.get_items():
            amt += i.get_price()

        amt += 0.18 * amt
        order.set_total_amt(amt)

    def max_discount(self, discount_strategy: DiscountStrategy, order: Order):
        order.set_total_amt(discount_strategy.apply(order.get_total_amt()))
