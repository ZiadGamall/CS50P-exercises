# Camel to Snake — Converts a camelCase variable name into snake_case.

def main():
    text = input("camelCase: ")
    convertedText = snakeCase(text)
    print(f"snake_case: {convertedText}")

def snakeCase(text):
    result = ""
    for letter in text:
        if letter.isupper():
            result += "_" + letter.lower()
        else:
            result += letter
        
    return result


main()