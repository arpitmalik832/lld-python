from projects.libraryManagementSystem.users.Member import Member


class Student(Member):

    def __init__(self, user_id, name, contact_info, student_id):
        super().__init__(user_id, name, contact_info, 5)
        self.__studentId = student_id

    def get_details(self):
        print("Student Id: " + str(self.__studentId))
        print("Name: " + self.get_name())
        print("Current Borrowed: " + str(self.get_current_borrowed()))

    # getter setters
    def get_student_id(self):
        return self.__studentId

    def set_student_id(self, student_id):
        self.__studentId = student_id
