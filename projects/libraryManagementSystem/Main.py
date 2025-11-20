from projects.libraryManagementSystem.items.books.HarryPotter import HarryPotter
from projects.libraryManagementSystem.users.Student import Student


def main():
    st = Student(1, "student 1", "student1@email.com", 1)
    st.get_details()
    hp = HarryPotter(2)

    hp.get_details()
    hp.lend_item(st)
    st.get_details()
    hp.get_details()

    hp.return_item(st)
    st.get_details()
    hp.get_details()

    hp.return_item(st)
    st.get_details()
    hp.get_details()


main()
