from projects.libraryManagementSystem.items.LendableItem import LendableItem
from projects.libraryManagementSystem.items.books.Book import Book
from projects.libraryManagementSystem.users.User import User


class HarryPotter(Book, LendableItem):
    def __init__(self, item_id):
        super().__init__(item_id, "HP1234", "Harry Potter", "Harry Potter author", True)

    def lend_item(self, user: User):
        if not user.can_borrow_books():
            print(user.get_name() + "cannot borrow books")
            return False

        if self.get_is_available():
            self.set_is_available(False)
            user.set_current_borrowed(user.get_current_borrowed() + 1)
            print(
                "Lending Harry Potter "
                + str(self.get_item_id())
                + " to "
                + user.get_name()
            )
            return True

        print("Harry Potter " + str(self.get_item_id()) + " is already lent out")
        return False

    def return_item(self, user: User):
        if not self.get_is_available():
            self.set_is_available(True)
            user.set_current_borrowed(user.get_current_borrowed() - 1)
            print(
                "Harry Potter "
                + str(self.get_item_id())
                + " is returned by "
                + user.get_name()
            )
            return

        print("Harry Potter " + str(self.get_item_id()) + " is already available")
