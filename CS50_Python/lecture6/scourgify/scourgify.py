import csv
import sys

try:
    file = sys.argv[2]
except IndexError:
    sys.exit ("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit ("Too many command-line arguments")

header = ["first", "secound", "house"]
data = []
try:
    with open (f'{sys.argv[1]}') as file:
        reader = csv.reader(file)
        head = next(reader)
        for row in reader:
            date = {}
            x, y = row[0].split(", ")
            z = row[1]
            date["first"] = y
            date["last"] = x
            date["house"] = z
            data.append(date)
except FileNotFoundError:
    sys.exit ("File does not exist")

with open (f'{sys.argv[2]}', "w", newline="") as one:
    writer = csv.DictWriter(one, fieldnames = date)
    writer.writeheader()
    writer.writerows(data)
