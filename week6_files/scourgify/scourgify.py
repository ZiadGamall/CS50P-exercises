# Scourgify - Converts a CSV of students' names and houses into a cleaner format with separate first and last name columns

import csv
import sys

if len(sys.argv) != 3:
    print(
        "Too many command-line arguments!"
        if len(sys.argv) > 3
        else "Too few command-line arguments!"
    )
    sys.exit(1)

readName = sys.argv[1]
writeName = sys.argv[2]

try:
    with open(readName) as readFile:
        rows = csv.DictReader(readFile)

        with open(writeName, "w", newline="") as writeFile:
            writer = csv.DictWriter(writeFile, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for row in rows:
                last, first = row["name"].split(",")
                writer.writerow(
                    {"first": first.strip(), "last": last, "house": row["house"]}
                )

except FileNotFoundError:
    print(f"Could not read {readName}")
    sys.exit(1)
