"""
Implement a function foo(List[int]) -> List[int] which, given a list of integers,
return a new list such that each element at index i of the new list is the product
of all the numbers in the original array except the one at i. Example:
foo([1, 2, 3, 4, 5])
[120, 60, 40, 30, 24]

foo([3, 2, 1])
[2, 3, 6]
"""

def transform(input_list):
    product = 1
    result = []

    for i in input_list:
        product *= i

    for i in input_list:
        result.append(product//i)

    return result


if __name__ == "__main__":
    print(transform([3, 2, 1]))
    print(transform([1, 2, 3, 4, 5]))
