def task1_4(input_dict):
    """
    ### Task 1.4
    Write a Python program to sort a dictionary by key.
    """
    return dict(sorted(input_dict.items()))


if __name__ == "__main__":
    print(task1_4({',': 1, ' ': 3, 'o': 2, 'h': 2, 'i': 2, 't': 2, 's': 1, 'p': 1, 'y': 1, 'n': 1}))
