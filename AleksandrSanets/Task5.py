def task1_5(input_list):
    """
    ### Task 1.5
    Write a Python program to print all unique values of all dictionaries in a list.
    Examples:
    Input: [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
    Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
    """
    values = []
    for item_dict in input_list:
        values.append(*item_dict.values())

    return set(values)


if __name__ == "__main__":
    print(task1_5([{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
                   {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},
                   {"VIII": "S007"}]))
