def split_by_index(num):
    """
    Implement a function get_digits(num: int) -> Tuple[int] which returns a tuple of a given integer's digits 
    """
    result = []
    for i in str(num):
        result.append(int(i))
    return tuple(result)


if __name__ == "__main__":
    print(split_by_index(87178291199))
    # (8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9)
