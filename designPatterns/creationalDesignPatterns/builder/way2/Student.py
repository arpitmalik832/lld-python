# Better way using inner class.
from designPatterns.creationalDesignPatterns.builder.exceptions.InvalidEmailException import (
    InvalidEmailException,
)
from designPatterns.creationalDesignPatterns.builder.exceptions.InvalidIntermediateMarksException import (
    InvalidIntermediateMarksException,
)
from designPatterns.creationalDesignPatterns.builder.exceptions.InvalidIntermediateYearException import (
    InvalidIntermediateYearException,
)
from designPatterns.creationalDesignPatterns.builder.exceptions.InvalidMobileException import (
    InvalidMobileException,
)
from designPatterns.creationalDesignPatterns.builder.exceptions.InvalidNameException import (
    InvalidNameException,
)
from designPatterns.creationalDesignPatterns.builder.validators import EmailValidator


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
            self.marks = args[2]
            self.roll = args[3]
            self.mobile = args[4]
            self.email = args[5]
            self.intermediateYear = args[6]
            self.intermediateMarks = args[7]
            self.intermediateRoll = args[8]
            self.intermediateSchool = args[9]

    class Builder:
        def __init__(self):
            self.id = None
            self.name = None
            self.marks = None
            self.roll = None
            self.mobile = None
            self.email = None
            self.intermediateYear = None
            self.intermediateMarks = None
            self.intermediateRoll = None
            self.intermediateSchool = None

        def set_id(self, id: str) -> "Student.Builder":
            self.id = id
            return self

        def set_name(self, name: str) -> "Student.Builder":
            self.name = name
            return self

        def set_marks(self, marks: int) -> "Student.Builder":
            self.marks = marks
            return self

        def set_roll(self, roll: str) -> "Student.Builder":
            self.roll = roll
            return self

        def set_mobile(self, mobile: str) -> "Student.Builder":
            self.mobile = mobile
            return self

        def set_email(self, email: str) -> "Student.Builder":
            self.email = email
            return self

        def set_intermediate_year(self, intermediate_year: int) -> "Student.Builder":
            self.intermediateYear = intermediate_year
            return self

        def set_intermediate_marks(self, intermediate_marks: int) -> "Student.Builder":
            self.intermediateMarks = intermediate_marks
            return self

        def set_intermediate_roll(self, intermediate_roll: str) -> "Student.Builder":
            self.intermediateRoll = intermediate_roll
            return self

        def set_intermediate_school(
            self, intermediate_school: str
        ) -> "Student.Builder":
            self.intermediateSchool = intermediate_school
            return self

        def validate(self):
            self.validate_name()
            self.validate_mobile()
            self.validate_email()
            self.validate_intermediate_year()
            self.validate_intermediate_marks()

        def validate_name(self):
            if self.name is None or len(self.name) == 0:
                raise InvalidNameException("Name cannot be empty")

        def validate_mobile(self):
            if self.mobile is None or len(self.mobile) == 0:
                raise InvalidMobileException("Mobile cannot be empty")

            if len(self.mobile) != 10:
                raise InvalidMobileException("Mobile number must be of 10 digits")

        def validate_email(self):
            if self.email is None or len(self.email) == 0:
                raise InvalidEmailException("Email cannot be empty")

            if not EmailValidator.is_valid(self.email):
                raise InvalidEmailException("Invalid email format")

        def validate_intermediate_year(self):
            if self.intermediateYear > 2022:
                raise InvalidIntermediateYearException(
                    "Only intermediate holders upto 2022 are allowed"
                )

        def validate_intermediate_marks(self):
            if self.intermediateMarks < 60:
                raise InvalidIntermediateMarksException(
                    "Intermediate marks cannot be less than 60"
                )

        def build(self) -> "Student":
            self.validate()
            return Student(self)
