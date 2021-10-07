a = "I am global variable!"


def enclosing_funcion_1():
    """Find a way to call inner_function without moving it from inside of enclosed_function."""

    a = "I am variable from enclosed function!"

    def inner_function():

        a = "I am local variable!"
        print(a)

    return inner_function()


enclosing_funcion_1()


def enclosing_funcion_2_1():
    """Modify ONE LINE in inner_function to make it print variable 'a' from global scope."""
    a = "I am variable from enclosed function!"

    def inner_function():

        global a

        print(a)

    return inner_function()


enclosing_funcion_2_1()


def enclosing_funcion_2_2():
    """Modify ONE LINE in inner_function to make it print variable 'a' form enclosing function."""
    a = "I am variable from enclosed function!"

    def inner_function():

        nonlocal a

        print(a)

    return inner_function()


enclosing_funcion_2_2()
