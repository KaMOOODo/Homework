from collections import Counter

def most_common_words(filepath, number_of_words=3):
    """Implement a function which search for most common words in the file."""
    with open(filepath) as f:
        data = f.read().split()

    clear_data(data)
    counted = Counter(data)
    most_common = counted.most_common(number_of_words)

    result = []
    for (x, _) in most_common:
        result.append(x)

    return result


def clear_data(data: list):
    for num, s in enumerate(data):
        data[num] = s.lower().strip(',.\n')

    return data

print(most_common_words("data/lorem_ipsum.txt"))
# ['donec', 'etiam', 'aliquam']
