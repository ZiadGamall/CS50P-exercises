# Line counter - Counts lines of actual Python code in a .py file, ignoring comments and blank lines

import sys

if len(sys.argv) != 2:
    print(
        "Too few command-line arguments!"
        if len(sys.argv) < 2
        else "Too many command-line arguments!"
    )
    sys.exit(1)

fileName = sys.argv[1]
if not fileName.endswith(".py"):
    print("Not a python file!")
    sys.exit(1)

lineCounter = 0

try:
    with open(fileName) as file:
        for line in file.readlines():
            strippedLine = line.strip()
            if strippedLine.startswith("#") or strippedLine == "":
                continue

            lineCounter += 1

except FileNotFoundError:
    print(f"{fileName} is not a file")
    sys.exit(1)

print(lineCounter)
