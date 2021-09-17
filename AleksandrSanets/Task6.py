def task1_6_2():
    """
    ### Task 1.6
    Write a program which makes a pretty print of a part of the multiplication table.
    Examples:
    Input:
    a = 2
    b = 4
    c = 3
    d = 7

    Output:
        3	4	5	6	7
    2	6	8	10	12	14
    3	9	12	15	18	21
    4	12	16	20	24	28
    """
    a = int(input("a: "))
    b = int(input("b: ")) + 1
    c = int(input("c: "))
    d = int(input("d: ")) + 1

    if a < b and c < d:
        for row in range(c, d):
            if row == c: print(end="\t")
            print(row, end="\t")
        print("")

        for i in range(a, b):
            print(i, end='\t')
            for j in range(c, d):
                print(j*i, end='\t')
            print("")
    else:
        print("a must be more than b and c is more than d")


if __name__ == "__main__":
    task1_6_2()
