# Twttr — Removes all vowels from user input to simulate shortened text.

vowels = ["a", "e", "i", "o", "u"]
text = input("Input: ")
result = ""
for letter in text:
    if letter.lower() not in vowels:
        result += letter

print(f"Output: {result}")