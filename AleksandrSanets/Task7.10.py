"""Implement a generator which will generate odd numbers endlessly."""


def endless_generator():
    count = 1
    while count > 0:
        yield count
        count += 2


if __name__ == "__main__":
    gen = endless_generator()
    while True:
        print(next(gen))
    # >>> 1 3 5 7 ... 128736187263 128736187265 ...
