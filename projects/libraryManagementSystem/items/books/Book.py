from projects.libraryManagementSystem.items.Item import Item


class Book(Item):
    def __init__(self, item_id, isbn, title, author, is_available):
        super().__init__(item_id)
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__isAvailable = is_available

    def get_details(self):
        print("Book title: " + self.__title)
        print("Book author: " + self.__author)
        print("Book isAvailable: " + str(self.__isAvailable))

    # getters setters
    def get_isbn(self):
        return self.__isbn

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_is_available(self):
        return self.__isAvailable

    def set_is_available(self, is_available):
        self.__isAvailable = is_available
