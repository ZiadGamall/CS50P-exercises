# Watch - Parses HTML to extract a YouTube embed URL and converts it to a shareable youtu.be link.

import re

def main():
    print(f"\nYoutube link: {parse(input("HTML: "))}")


def parse(s):
    if linkID := re.search(r"https?://(?:www\.)?youtube\.com/embed/(\w+)", s, re.IGNORECASE):
        return f"https://youtu.be/{linkID.group(1)}"
    return None


if __name__ == "__main__":
    main()