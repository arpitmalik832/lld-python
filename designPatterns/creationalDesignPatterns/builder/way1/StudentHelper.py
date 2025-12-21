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


class StudentHelper:
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

    # setter methods
    def set_id(self, id: str) -> "StudentHelper":
        self.id = id
        return self

    def set_name(self, name: str) -> "StudentHelper":
        self.name = name
        return self

    def set_marks(self, marks: int) -> "StudentHelper":
        self.marks = marks
        return self

    def set_roll(self, roll: str) -> "StudentHelper":
        self.roll = roll
        return self

    def set_mobile(self, mobile: str) -> "StudentHelper":
        self.mobile = mobile
        return self

    def set_email(self, email: str) -> "StudentHelper":
        self.email = email
        return self

    def set_intermediate_year(self, intermediate_year: int) -> "StudentHelper":
        self.intermediateYear = intermediate_year
        return self

    def set_intermediate_marks(self, intermediate_marks: int) -> "StudentHelper":
        self.intermediateMarks = intermediate_marks
        return self

    def set_intermediate_roll(self, intermediate_roll: str) -> "StudentHelper":
        self.intermediateRoll = intermediate_roll
        return self

    def set_intermediate_school(self, intermediate_school: str) -> "StudentHelper":
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
