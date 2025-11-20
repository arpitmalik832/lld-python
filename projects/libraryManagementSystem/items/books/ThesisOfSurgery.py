from projects.libraryManagementSystem.items.books.Book import Book


class ThesisOfSurgery(Book):
    def __init__(self, item_id, isbn, title, author, is_available):
        super().__init__(item_id, isbn, title, author, is_available)
