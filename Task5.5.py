def remember_result(func):
    """Implement a decorator remember_result which
    remembers last result of function it decorates
    and prints it before next call."""
    last_result = None

    def wrapper(*args):

        nonlocal last_result
        print(f"Last result = '{last_result}'")
        last_result = func(*args)

    return wrapper


@remember_result
def sum_list(*args):
    if isinstance(args[0], str):
        result = ""
    if isinstance(args[0], int):
        result = 0
    for item in args:
        result += item
    print(f"Current result = '{result}'")

    return result




sum_list("a", "b")
# >>> "Last result = 'None'"
# >>> "Current result = 'ab'"
sum_list("abc", "cde")
# >>> "Last result = 'ab'"
# >>> "Current result = 'abccde'"
sum_list(3, 4, 5)
# >>> "Last result = 'abccde'"
# >>> "Current result = '12'"
