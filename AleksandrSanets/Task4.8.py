def get_pairs(lst: list) -> list:
    """Implement a function get_pairs(lst: List) -> List[Tuple] which
    returns a list of tuples containing pairs of elements.
    Pairs should be formed as in the example.
    If there is only one element in the list return None instead.
    """
    pairs = []
    if len(lst) == 1:
        return None
    for num, i in enumerate(lst):
        if i != lst[-1]:
            pair = (lst[num], lst[num+1])
            pairs.append(pair)

    return pairs


if __name__ == "__main__":
    print(get_pairs([1, 2, 3, 8, 9]))
    # [(1, 2), (2, 3), (3, 8), (8, 9)]

    print(get_pairs(['need', 'to', 'sleep', 'more']))
    # [('need', 'to'), ('to', 'sleep'), ('sleep', 'more')]

    print(get_pairs([1]))
    # None
