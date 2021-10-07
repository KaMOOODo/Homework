"""Implement decorator for supressing exceptions. If exception not occure write log to console."""

from functools import wraps


def supressing_exceptions(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except Exception:
            return None
        else:
            print(f"{func.__name__} - finished")
            return result

    return wrapper


@supressing_exceptions
def same_function():
    return print(2/0)


@supressing_exceptions
def same_function1():
    return print(2/2)


if __name__ == "__main__":
    same_function()
    same_function1()
