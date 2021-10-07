def call_once(func):
    """
        Implement a decorator call_once which runs a function or
        method once and caches the result. All consecutive calls to
        this function should return cached result no matter the arguments.
    """
    first_result = None

    def wrapper(*args):

        nonlocal first_result

        if not first_result:
            first_result = func(*args)

        return first_result

    return wrapper


@call_once
def sum_of_numbers(a, b):
    return a + b


print(sum_of_numbers(13, 42))
# >>> 55
print(sum_of_numbers(999, 100))
# >>> 55
print(sum_of_numbers(134, 412))
# >>> 55
print(sum_of_numbers(856, 232))
# >>> 55
