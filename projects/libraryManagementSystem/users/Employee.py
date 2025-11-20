from projects.libraryManagementSystem.users.User import User


class Employee(User):
    def __init__(self, user_id, name, contact_info, employee_id):
        super().__init__(user_id, name, contact_info)
        self.__employeeId = employee_id

    def get_details(self):
        print("Employee Id: " + self.__employeeId)
        print("Name: " + self.get_name())
        print("Contact Info: " + self.get_contact_info())

    def can_borrow_books(self):
        return True

    # getter setters
    def get_employee_id(self):
        return self.__employeeId

    def set_employee_id(self, employee_id):
        self.__employeeId = employee_id
