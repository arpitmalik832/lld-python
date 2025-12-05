import heapq
from dataclasses import dataclass


@dataclass
class Order:
    order_id: str
    item_id: str
    quantity: int
    is_express: bool

    def __lt__(self, other) -> bool:
        if self.is_express == other.is_express:
            return self.order_id < other.order_id
        elif self.is_express:
            return True
        else:
            return False


class OrderProcessor:
    def __init__(self):
        self.orders = []

    def add(self, order: Order):
        heapq.heappush(self.orders, order)

    def get_next_order(self):
        if not self.orders:
            return None
        return self.orders[0]
