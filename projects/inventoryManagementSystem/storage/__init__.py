from collections import deque
from typing import Generic, TypeVar

from projects.inventoryManagementSystem.items import Item

T = TypeVar("T", bound=Item)


class SearchHistory:
    def __init__(self):
        self.deque = deque()
        self.MAX_ALLOWED = 3

    def add(self, item: Item):
        if self.deque.__contains__(item.get_id()):
            self.deque.remove(item)
        self.deque.appendleft(item)
        if len(self.deque) > self.MAX_ALLOWED:
            self.deque.pop()

    def remove(self, target_id):
        self.deque = deque(item for item in self.deque if item.get_id() != target_id)

    def get_history(self) -> list[Item]:
        return list(self.deque)


class Inventory(Generic[T]):
    def __init__(self, search_history: SearchHistory):
        self.items: dict[str, T] = {}
        self.search_history = search_history

    def add(self, item: T):
        if item is None:
            # throw IllegalArgumentException("Item cannot be null");
            pass
        if item.get_id() is None:
            # throw new IllegalArgumentException("Item id cannot be null");
            pass
        if item.get_id() in self.items:
            # throw new IllegalArgumentException("Item with id " + item.getId() + " already exists");
            pass
        self.items[item.get_id()] = item
        print("Item added to inventory : " + item.get_name())

    def remove(self, id: str):
        if id is None:
            # throw new IllegalArgumentException("Item id cannot be null");
            pass
        self.search_history.remove(id)
        del self.items[id]
        # if (item == null) {
        #     throw new IllegalArgumentException("Item with id " + id + " does not exist");
        # }

    def get(self, id: str) -> T:
        if id is None:
            #   throw new IllegalArgumentException("Item id cannot be null");
            pass
        item = self.items[id]
        if item is None:
            # throw new IllegalArgumentException("Item with id " + id + " does not exist");
            pass
        self.search_history.add(item)
        print("Got item : " + item.get_name())
        return item

    def get_all(self) -> list[T]:
        return list(self.items.values())
