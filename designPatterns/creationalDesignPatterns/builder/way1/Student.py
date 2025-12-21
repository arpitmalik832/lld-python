from designPatterns.creationalDesignPatterns.builder.way1.StudentHelper import (
    StudentHelper,
)


class Student:
    def __init__(self, *args):
        if len(args) == 1:
            self.__init__(
                args[0].id,
                args[0].name,
                args[0].marks,
                args[0].roll,
                args[0].mobile,
                args[0].email,
                args[0].intermediateYear,
                args[0].intermediateMarks,
                args[0].intermediateRoll,
                args[0].intermediateSchool,
            )
        elif len(args) == 10:
            self.__id = args[0]
            self.__name = args[1]
            self.__marks = args[2]
            self.__roll = args[3]
            self.__mobile = args[4]
            self.__email = args[5]
            self.__intermediateYear = args[6]
            self.__intermediateMarks = args[7]
            self.__intermediateRoll = args[8]
            self.__intermediateSchool = args[9]

    @staticmethod
    def build(helper: "StudentHelper") -> "Student":
        helper.validate()
        return Student(helper)
