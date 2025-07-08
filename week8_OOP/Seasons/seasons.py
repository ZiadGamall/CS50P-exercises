# Seasons - Calculates and prints a person’s age in minutes, written out in English words.


import datetime
import inflect
import sys


def main():
    date = input("Date of birth: ")
    days = (datetime.date.today() - get_date(date)).days
    minutes = days * 24 * 60
    print(f"{stringify(minutes)} minutes")


def get_date(date):
    try:
        return datetime.date.fromisoformat(date)
    except ValueError:
        print("Invalid date")
        sys.exit(1)


def stringify(num):
    text = inflect.engine().number_to_words(num, andword="")
    return text.capitalize()


if __name__ == "__main__":
    main()
