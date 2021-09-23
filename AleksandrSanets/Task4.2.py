def is_palindrome(string):
    """
    Write a function that check whether a string is a palindrome or not.
    Usage of any reversing functions is prohibited.
    """
    if isinstance(string, str):
        n = len(string) - 1
        i = 0
        while n > i:
            if string[n] != string[i]:
                return False
            else:
                i += 1
                n -= 1
        return True
    else:
        print("argument must be a string")


if __name__ == "__main__":
    print(is_palindrome("lodol"))
