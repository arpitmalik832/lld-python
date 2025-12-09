# Do not modify this code
class InvalidBookNameException(Exception):
    pass


# TODO: Implement the validate method inside the BookNameValidator class
class BookNameValidator:
    @staticmethod
    def validate(book_name: str):
        if book_name.startswith("Scaler Java"):
            print("Book created!:" + book_name)
        else:
            raise InvalidBookNameException("Book name doesn't start with Scaler Java")


# BookNameValidator.validate("Java for Scalers")
BookNameValidator.validate("Scaler Java 2")


class DivisionByZeroError(Exception):
    # Custom exception is raised when attempting to divide by zero.
    # don't modify this custom exception class
    pass


# TODO : raise DivisionByZeroError if divisor is zero, return result otherwise
def divide_numbers(dividend, divisor):
    # Complete the code
    try:
        return dividend / divisor
    except ZeroDivisionError:
        raise DivisionByZeroError("Divisor cannot be zero")
