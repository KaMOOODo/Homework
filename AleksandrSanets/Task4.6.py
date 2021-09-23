def get_shortest_word(s: str) -> str:
    """Implement a function get_shortest_word(s: str) -> str which
    returns the longest word in the given string. The word can contain any symbols
    except whitespaces ( , \n, \t and so on). If there are multiple longest words
    in the string with a same length return the word that occures first. Example:
    """
    separators = [" ", "\n", "\t", "\r", "\b"]
    indexes = [0, ]

    for num, i in enumerate(s):
        if i in separators:
            indexes.append(num)

    indexes.append(len(s))
    max_len = 0
    i = len(indexes) - 1
    while i >= 0:
        len_word = indexes[i] - indexes[i-1]
        if len_word >= max_len:
            max_len = len_word
            max_end_index = i
        i -= 1

    return (s[indexes[max_end_index - 1]:indexes[max_end_index]]).strip()


if __name__ == "__main__":
    print(get_shortest_word('Python is simple and effective!'))
    # 'effective!'

    print(get_shortest_word('Any pythonista like namespaces a lot.'))
    # 'pythonista'