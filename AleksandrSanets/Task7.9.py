"""Implement an iterator class EvenRange, which accepts start and end of the interval
as an init arguments and gives only even numbers during iteration.
If user tries to iterate after it gave all possible numbers `Out of numbers!` should be printed.
_Note: Do not use function `range()` at all_"""


class EvenRange:
    def __init__(self, start, end):
        self.start = start if start % 2 == 0 else start + 1
        self.end = end
        self.flag = False

    def __iter__(self):
        self.flag = True
        return self

    def __next__(self):

        if self.start <= self.end:
            self.even = self.start
            self.start += 2
            return self.even
        if self.flag:
            print("Out of numbers!")
            raise StopIteration
        else:
            return "Out of numbers!"


if __name__ == "__main__":
    er1 = EvenRange(7,11)
    print(next(er1))
    # >>> 8
    print(next(er1))
    # >>> 10
    print(next(er1))
    # >>> "Out of numbers!"
    print(next(er1))
    # >>> "Out of numbers!"
    er2 = EvenRange(3, 14)
    for number in er2:
        print(number)
# >>> 4 6 8 10 12 "Out of numbers!"