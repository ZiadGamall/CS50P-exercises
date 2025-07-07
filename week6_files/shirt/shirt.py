# Shirt - Overlays a shirt image onto a resized and cropped input photo, preserving transparency, and saves the result.

import sys
from PIL import Image,ImageOps

if len(sys.argv) != 3:
    print(
        "Too many command-line arguments!"
        if len(sys.argv) > 3
        else "Too few command-line arguments!"
    )
    sys.exit(1)

inputFile = sys.argv[1]
outputFile = sys.argv[2]
inputSuffix = inputFile.split(".")[1].lower()
outputSuffix = outputFile.split(".")[1].lower()

extensions = ["jpg", "jpeg", "png"]

if inputSuffix not in extensions or outputSuffix not in extensions:
    print("Inavlid input!")
    sys.exit(1)

if inputSuffix != outputSuffix:
    print("Input and output have different extensions!")
    sys.exit(1)

try:
    with Image.open(inputFile) as img:
        with Image.open("shirt.png") as shirt:
           resized = ImageOps.fit(img, shirt.size)
           resized.paste(shirt, shirt)
           resized.save(outputFile)
except FileNotFoundError:
    print("Invalid input file!")
    sys.exit(1)