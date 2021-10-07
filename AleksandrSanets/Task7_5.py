"""
Implement function for check that number is even and is greater than 2. Throw different exceptions for this errors.
Custom exceptions must be derived from custom base exception(not Base Exception class).
"""


class CustomException(Exception):
    pass


class IsNotGreaterThanTwo(CustomException):
    pass


class NumberIsNotEven(CustomException):
    pass


def is_even_and_greater_than_two(number: int):
    if number <= 2:
        raise IsNotGreaterThanTwo
    elif number % 2 != 0:
        raise NumberIsNotEven

    if number % 2 == 0 and number > 2:
        return True


if __name__ == "__main__":
    print(is_even_and_greater_than_two(1))