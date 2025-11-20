from projects.libraryManagementSystem.users.Member import Member


class Professor(Member):
    def __int__(self, user_id, name, contact_info, professor_id):
        super().__init__(user_id, name, contact_info, 15)
        self.__professorId = professor_id

    def get_details(self):
        print("Professor Id: " + self.__professorId)
        print("Name: " + self.get_name())
        print("Current Borrowed: " + self.get_current_borrowed())

    # getter setters
    def get_professor_id(self):
        return self.__professorId

    def set_professor_id(self, professor_id):
        self.__professorId = professor_id
