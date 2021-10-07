
"""Implement class-based context manager for opening and working with file, including handling exceptions.
Do not use 'with open()'. Pass filename and mode via constructor."""


class MyOpen:
    def __init__(self, path, mode="r"):
        self.__path = path
        self.__mode = mode
        self.__file = None

    def __enter__(self):
        try:
            self.__file = open(self.__path, self.__mode)
        except OSError as os_error:
            print(f"Can't open the file:\tOSError: {os_error}")
        else:
            return self.__file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.__file:
            self.__file.close()
        if exc_type:
            print(f"Can't close the file:\t{exc_val}")
        return True

    def __repr__(self):
        return f"MyOpen({self.__path, self.__mode})"


if __name__ == "__main__":
    with MyOpen(path="README.md") as file:
        print(file.read())
