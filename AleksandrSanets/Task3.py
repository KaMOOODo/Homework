def task1_3_1(string):
    """
    Task 1.3
    Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form.
    Examples:
    Input: ['red', 'white', 'black', 'red', 'green', 'black']
    Output: ['black', 'green', 'red', 'white', 'red']
    """
    # string = input("Input a comma separated sequence of words:")
    string = sorted(list(set(string.split(","))))
    return string


def task1_3_2(number):
    """
    Task 1.3
    Create a program that asks the user for a number and then prints out a list of all the [divisors](https://en.wikipedia.org/wiki/Divisor) of that number.
    Examples:
    Input: 60
    Output: {1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60}
    """
    # number = input("Input a number: ")
    divisors = [1, ]
    for i in range(2, number + 1):
        if number % i == 0:
            divisors.append(i)

    return set(divisors)


if __name__ == "__main__":
    print(task1_3_1("red,white,black,red,green,black"))
    print(task1_3_2(60))
