from abc import ABC, abstractmethod


class Item(ABC):
    def __init__(self, item_id):
        self.__itemId = item_id

    @abstractmethod
    def get_details(self):
        pass

    def get_item_id(self):
        return self.__itemId
