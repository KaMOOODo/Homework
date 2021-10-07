# Implement your custom iterator class called MySquareIterator
# which gives squares of elements of collection it iterates through.


class MySquareIterator:
    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i < len(self.lst):
            i_sqr = self.lst[self.i] ** 2
            self.i += 1
            return i_sqr
        else:
            raise StopIteration


if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5]
    itr = MySquareIterator(lst)
    for item in itr:
        print(item)
    # >>> 1 4 9 16 25
