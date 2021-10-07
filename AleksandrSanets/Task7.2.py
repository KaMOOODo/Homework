"""Implement context manager for opening and working with file,
including handling exceptions with @contextmanager decorator."""

from contextlib import contextmanager


@contextmanager
def my_open(path, mode="r"):
    _file = open(path, mode)
    try:
        print(f"def my_open successfully opened the file '{_file.name}'")
        yield _file

    except OSError as os_error:
        print(f"Can't open the file:\tOSError: {os_error}")
    finally:
        _file.close()
        print(f"def my_open successfully closed the file '{_file.name}'")


if __name__ == "__main__":
    with my_open("README.md") as file:
        print(file.read())
