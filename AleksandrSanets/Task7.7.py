"""Implement your custom collection called MyNumberCollection. It should be able to contain only numbers.
It should NOT inherit any other collections.

If user tries to add a string or any non numerical object there, exception `TypeError` should be raised.

Method init should be able to take either `start,end,step` arguments, where `start` - first number of collection,
`end` - last number of collection or some ordered iterable collection (see the example).

Implement following functionality:
* appending new element to the end of collection
* concatenating collections together using `+`
* when element is addressed by index(using `[]`), user should get square of the addressed element.
* when iterated using cycle `for`, elements should be given normally
* user should be able to print whole collection as if it was list."""


class MyNumberCollection:
    def __init__(self, start, end=None, step=None):
        self.start = start
        self.end = end
        self.step = step
        self._list = self.create_list()

    def create_list(self):
        __list = []
        if isinstance(self.start, (int, float)):
            for number in range(self.start, self.end, self.step):
                __list.append(number)
            __list.append(self.end)
        elif isinstance(self.start, (list, tuple, set)):
            for number in self.start:
                if isinstance(number, (int, float)):
                    __list.append(number)
                else:
                    raise TypeError(f"'{number}' - non numerical object")
        else:
            raise TypeError(f"'{self.start}' - non numerical object")
        return __list

    def append(self, add_number):
        if isinstance(add_number, (int, float)):
            self._list.append(add_number)
        else:
            raise TypeError(f"'{add_number}' - object is not a number!")

    def __str__(self):
        return str(self._list)

    def __add__(self, other):
        if isinstance(other, MyNumberCollection):
            return self._list + other._list
        else:
            raise TypeError

    def __radd__(self, other):
        return other._list + self._list

    def __getitem__(self, index):
        return self._list[index] ** 2

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start < len(self._list):
            return self._list[self.start]
        else:
            raise StopIteration


if __name__ == "__main__":
    col1 = MyNumberCollection(0, 5, 2)
    print(col1)
    # >>> [0, 2, 4, 5]
    col2 = MyNumberCollection((1,2,3,4,5))
    print(col2)
    # >>> [1, 2, 3, 4, 5]

    # col3 = MyNumberCollection((1,2,3,"4",5))
    # >>> TypeError: MyNumberCollection supports only numbers!

    col1.append(7)
    print(col1)
    # >>> [0, 2, 4, 5, 7]

    # col2.append("string")
    # >>> TypeError: 'string' - object is not a number!

    print(col1 + col2)
    # >>> [0, 2, 4, 5, 7, 1, 2, 3, 4, 5]

    print(col1)
    # >>> [0, 2, 4, 5, 7]

    print(col2)
    # >>> [1, 2, 3, 4, 5]

    print(col2[4])
    # >>> 25

    for item in col1:
        print(item)
    # >>> 0 2 4 5 7
