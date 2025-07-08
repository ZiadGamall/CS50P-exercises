# Word counter - Counts how many times a user-input word appears in a line of text, case-insensitively.

import re


def main():
    word = input("Enter the word you want to count: ")
    text = input("Text: ")
    print(count(word, text))

def count(w, s):
    escaped_word = re.escape(w.lower())
    s = s.lower()

    # If the word is purely alphanumeric, use word boundaries
    if w.isalnum():
        pattern = fr"\b{escaped_word}\b"
    else:
        # No word boundaries for symbols like '?', 'C++', etc.
        pattern = escaped_word

    return len(re.findall(pattern, s))



if __name__ == "__main__":
    main()