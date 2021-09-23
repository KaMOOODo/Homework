def replace_quotes(string):
    """This function replaces all " symbols with ' and vise versa."""

    if isinstance(string, str):

        if not string.count("'") and not string.count('"'):
            print("string has not a quotes")

        list_of_chars = []

        for i in string:
            if i != "'" and i != '"':
                list_of_chars.append(i)
            if i == "'":
                list_of_chars.append('"')
            if i == '"':
                list_of_chars.append("'")

        return ''.join(list_of_chars)

    else:
        print("argument must be a string")


if __name__ == "__main__":
    print(replace_quotes("""all "'" symbols with ' and """))
