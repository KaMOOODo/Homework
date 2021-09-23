import string
test_strings = ["hello", "world", "python", ]


def test_1_1(*strings):
    """
    Implement a bunch of functions which receive a changeable number of
    strings and return characters that appear in all strings
    """
    return set(strings[0]).intersection(*strings)


print(test_1_1(*test_strings))
# >>> {'o'}


def test_1_2(*strings):
    """
    Implement a bunch of functions which receive a changeable number of
    strings and return characters that appear in at least one string
    """
    return set(strings[0]).union(*strings)


print(test_1_2(*test_strings))
# >>> {'d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y'}


def test_1_3(*strings):
    """
    Implement a bunch of functions which receive a changeable number of
    strings and return characters that appear at least in two strings
    """
    dbl = set()
    for word in strings:
        for word2 in strings:
            if word != word2:
                dbl.update({*word}.intersection({*word2}))

    return dbl


print(test_1_3(*test_strings))
# # >>> {'h', 'l', 'o'}


def test_1_4(*strings):
    """
    Implement a bunch of functions which receive a changeable number of
    strings and return characters of alphabet, that were not used in any string
    """
    alphabet = set(string.ascii_lowercase)
    unique_symbols = set(strings[0]).union(*strings)
    return alphabet - unique_symbols


print(test_1_4(*test_strings))
# >>> {'a', 'b', 'c', 'f', 'g', 'i', 'j', 'k', 'm', 'q', 's', 'u', 'v', 'x', 'z'}
