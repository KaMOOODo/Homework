def str_split(string: str, separtor=" ", maxsplit=-1):
    """Implement a function which works the same as str.split method"""
    if isinstance(string, str):
        counter = 0
        splitted_string = []
        flag = 0
        len_sep = len(separtor)
        for num, i in enumerate(string):
            if counter == maxsplit:
                return splitted_string
            if i == separtor[0] and len_sep > 1:
                if separtor == string[num:num+len_sep]:
                    splitted_string.append(string[flag:num])
                    flag = num + len_sep
                    counter += 1
            if i == separtor:
                splitted_string.append(string[flag:num])
                flag = num + 1
                counter += 1
        if flag != len(string):
            splitted_string.append(string[flag:])
        return splitted_string

    else:
        print("argument must be a string")


if __name__ == "__main__":
    print(str_split("1, 2, 3 4", separtor=", ", maxsplit=2))
