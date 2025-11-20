from abc import ABC

from projects.libraryManagementSystem.users.User import User


class Member(User, ABC):
    def __init__(self, user_id, name, contact_info, max_borrow_limit):
        super().__init__(user_id, name, contact_info)
        self.__MAX_BORROW_LIMIT = max_borrow_limit

    def can_borrow_books(self):
        return self.get_current_borrowed() < self.__MAX_BORROW_LIMIT

    # getter setter
    def get_max_borrow_limit(self):
        return self.__MAX_BORROW_LIMIT

    def set_max_borrow_limit(self, max_borrow_limit):
        self.__MAX_BORROW_LIMIT = max_borrow_limit
