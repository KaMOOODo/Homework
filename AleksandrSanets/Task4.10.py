def generate_squares(x):
    """
    Implement a function that takes a number as an argument and returns a dictionary,
    where the key is a number and the value is the square of that number.
    """
    result = {x: x ** 2 for x in range(1, x+1)}

    return result


if __name__ == "__main__":
    print(generate_squares(5))