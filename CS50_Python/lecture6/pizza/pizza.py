from tabulate import tabulate
import csv
import sys

try:
    file = sys.argv[1]

except IndexError:
    sys.exit ("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit ("Too many command-line arguments")

if (file[-4:]) == ".csv":
    try:
        with open (f"{file}") as csvfile:
            reader = csv.reader(csvfile)
            print (tabulate(reader, headers='firstrow',tablefmt='grid'))
    except FileNotFoundError:
        sys.exit ("File does not exist")
else:
    sys.exit ("Not a CSV file")

