# Pizza menu - Displays a CSV pizza menu as a formatted ASCII table using tabulate

from csv import DictReader
from tabulate import tabulate
import sys

if len(sys.argv) != 2:
    print(
        "Too few command-line arguments!"
        if len(sys.argv) < 2
        else "Too many command-line arguments!"
    )
    sys.exit(1)

fileName = sys.argv[1]

if not fileName.endswith(".csv"):
    print("Not a csv file!")
    sys.exit(1)

try:
    with open(fileName) as file:
        lines = DictReader(file)
        # print(tabulate(lines, headers="keys", tablefmt="grid"))
        for row in lines:
            print(row)
except FileNotFoundError:
    print(f"{fileName} is not a file!")
    sys.exit(1)
