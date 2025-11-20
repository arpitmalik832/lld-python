from projects.libraryManagementSystem.items.Item import Item


class Magazine(Item):
    def __int__(self, item_id):
        super().__init__(item_id)

    def get_details(self):
        print("Magazine Details")
