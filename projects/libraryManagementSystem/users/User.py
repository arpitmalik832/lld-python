from abc import ABC, abstractmethod


class User(ABC):
    # parameterized constructor
    def __init__(self, user_id, name, contact_info):
        self.__userId = user_id
        self.__name = name
        self.__contactInfo = contact_info
        self.__currentBorrowed = 0

    @abstractmethod
    def get_details(self):
        pass

    @abstractmethod
    def can_borrow_books(self):
        pass

    # public getters and setters
    def get_user_id(self):
        return self.__userId

    def set_user_id(self, user_id):
        self.__userId = user_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_contact_info(self):
        return self.__contactInfo

    def set_contact_info(self, contact_info):
        self.__contactInfo = contact_info

    def get_current_borrowed(self):
        return self.__currentBorrowed

    def set_current_borrowed(self, current_borrowed):
        self.__currentBorrowed = current_borrowed
