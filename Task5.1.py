with open("data/unsorted_names.txt") as f:
    unsorted_names = list(f)
    unsorted_names.sort()

with open("sorted_names.txt", mode="w") as f:
    f.write("".join(unsorted_names))
