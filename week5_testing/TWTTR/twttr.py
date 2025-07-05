# Twttr — Removes all vowels from user input to simulate shortened text.

def main():
    text = input("Input: ")
    print(f"Output: {shorten(text)}")

def shorten(text):
    vowels = "aeiou"
    return "".join([char for char in text if char.lower() not in vowels])

if __name__ == "__main__":
    main()