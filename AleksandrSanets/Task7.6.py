"""
Create console program for proving Goldbach's conjecture. Program accepts number for input and print result.
For pressing 'q' program succesfully close. Use function from Task 5.5 for validating input,
handle all exceptions and print user friendly output.
"""
from Task7_5 import is_even_and_greater_than_two, IsNotGreaterThanTwo, NumberIsNotEven


def is_prime(number):
    for num in range(2, number):
        if number % num == 0:
            return False
    return True


def conjecture_of_goldbach():
    while True:
        u_input = input("Enter a number or 'q' to quit: ")
        if u_input == "q":
            print("Bye!")
            return None
        try:
            number = int(u_input)
        except ValueError:
            print(f"Try to enter even integer")
            continue
        try:
            is_even_and_greater_than_two(number)
            for i in range(1, number):
                j = number - i
                if is_prime(i) and is_prime(j):
                    print(f"Possible variant of a pair is {i} and {j}")
                    return None
        except NumberIsNotEven:
            print("Try to enter even integer")
        except IsNotGreaterThanTwo:
            print("Try to enter even integer greater than 2")
        else:
            return None


if __name__ == "__main__":
    conjecture_of_goldbach()