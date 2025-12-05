from projects.inventoryManagementSystem.items import Book, Clothing, Electronic
from projects.inventoryManagementSystem.shipping import Order, OrderProcessor
from projects.inventoryManagementSystem.storage import SearchHistory, Inventory


class Main:
    def __init__(self):
        self.searchHistory = SearchHistory()
        self.booksInventory = Inventory(self.searchHistory)
        self.clothingsInventory = Inventory(self.searchHistory)
        self.electronicsInventory = Inventory(self.searchHistory)


def main():
    system = Main()

    system.booksInventory.add(Book("1", "Book 1", 9.99, 10, "Author 1"))
    system.booksInventory.add(Book("2", "Book 2", 9.99, 10, "Author 2"))

    system.electronicsInventory.add(Electronic("1", "Electronic 1", 9.99, 10, 100))
    system.electronicsInventory.add(Electronic("2", "Electronic 2", 9.99, 10, 100))

    system.clothingsInventory.add(Clothing("1", "Clothing 1", 9.99, 10, "S"))
    system.clothingsInventory.add(Clothing("2", "Clothing 2", 9.99, 10, "M"))

    system.booksInventory.get("1")
    system.electronicsInventory.get("2")
    system.booksInventory.get("2")
    system.clothingsInventory.get("1")
    system.electronicsInventory.get("1")
    system.booksInventory.get("2")

    print(system.searchHistory.get_history())

    processor = OrderProcessor()

    # Adding orders
    processor.add(Order("103", "itemA", 1, False))  # Non-Express
    processor.add(Order("101", "itemB", 2, True))  # Express (Should be first)
    processor.add(Order("102", "itemC", 1, True))  # Express (Should be second by ID)

    # Peek
    next_order = processor.get_next_order()
    print(f"Next Order: {next_order.order_id}, Express: {next_order.is_express}")


main()
