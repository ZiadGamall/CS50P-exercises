# Bank — Analyzes user greeting to determine a cash reward based on how the greeting starts.

def main():
    print(value(input("Greeting: ")))

def value(greeting):
    greeting = greeting.strip().lower()
    if(greeting.startswith("hello")):
        return "$0"
    elif(greeting.startswith("h")):
        return "$20"
    else:
        return "$100"

if __name__ == "__main__":
    main()