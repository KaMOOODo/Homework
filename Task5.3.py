import csv


def get_top_performers(file_path, number_of_top_students=5):
    """Implement a function which receives file path and returns names of top performer students"""
    reader = csv.reader(open(file_path, 'r'))

    top = sorted(reader, key=lambda x: x[2], reverse=True)[1:number_of_top_students+1]

    result = []

    for i in top:
        result.append(i[0])

    return result


print(get_top_performers("data/students.csv"))
# ['Teresa Jones', 'Richard Snider', 'Jessica Dubose', 'Heather Garcia', 'Joseph Head']


def order_by_age(file_path_read, file_path_write="order_by_age.csv"):
    """Implement a function which receives the file path with students info and
    writes CSV student information to the new file in descending order of age."""
    reader = csv.reader(open(file_path_read, 'r'))

    ordered = sorted(reader, key=lambda x: x[1], reverse=True)

    with open(file_path_write, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(ordered)

    return True

print(order_by_age("data/students.csv"))