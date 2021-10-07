"""Implement decorator with context manager support for writing execution time to log-file. See contextlib module."""

from contextlib import ContextDecorator
from time import time, sleep


class WriteExecutionTimeToLogFile(ContextDecorator):
    def __enter__(self):
        self.t_start = time()
        return self

    def __exit__(self, *exc):
        self.t_end = time()
        with open("log.txt", mode="a") as log_file:
            log_file.write("Execution time: {:.5f}\n".format(self.t_end - self.t_start))
        return False


@WriteExecutionTimeToLogFile()
def same_function():
    print('Magic is here!')
    sleep(3)


if __name__ == "__main__":
    same_function()
