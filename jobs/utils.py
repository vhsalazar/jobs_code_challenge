import csv


def read_csv(file_path):
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            yield row  # Use a generator to return each row instead of allocating the whole list in memory
