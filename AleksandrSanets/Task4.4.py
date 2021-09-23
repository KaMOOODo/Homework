def split_by_index(s: str, indexes: list) -> list:
    """
    Implement a function split_by_index(s: str, indexes: list[int]) -> list[str]
    which splits the s string by indexes specified in indexes. Wrong indexes must be ignored.
    """
    result = []
    flag = 0

    for i in indexes:
        if i >= len(s):
            return [s]
        result.append(s[flag:i])
        flag = i

    if flag != len(s):
        result.append(s[flag:])
        
    return result

print(split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]))
# ["python", "is", "cool", ",", "isn't", "it?"]

print(split_by_index("no luck", [7]))
# ["no luck"]