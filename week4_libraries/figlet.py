# Figlet — Renders user input as ASCII art using a random or specified font via command-line arguments.

import pyfiglet
import sys
import random

if len(sys.argv) == 3:
    if sys.argv[1] != "-f" and sys.argv[1] != "--font":
        print("Invalid usage.")
        sys.exit()
    
    try:
        f = pyfiglet.Figlet(font=sys.argv[2])
    except pyfiglet.FontNotFound:
        print("Invalid usage.")
        sys.exit()

elif len(sys.argv) == 1:
    f = pyfiglet.Figlet()
    fonts = f.getFonts()
    f.setFont(font=random.choice(fonts))

else:
    print("Incorrect usage.")
    sys.exit()

text = input("Input: ")
print(f.renderText(text))