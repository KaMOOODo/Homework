def task1_1(string):
    """
    Task 1.1
    Write a Python program to calculate the length of a string without using the `len` function.
    """
    for num, i in enumerate(string):
        len_string = num
    return len_string + 1


if __name__ == "__main__":
    print(task1_1("### Task 1.1"))
