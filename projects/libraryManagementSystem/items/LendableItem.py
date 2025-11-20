from abc import ABC, abstractmethod

from projects.libraryManagementSystem.users.User import User


class LendableItem(ABC):
    @abstractmethod
    def lend_item(self, user: User):
        pass

    @abstractmethod
    def return_item(self, user: User):
        pass
