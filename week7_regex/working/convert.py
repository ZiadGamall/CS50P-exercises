# Converter - Parses a string representing a 12-hour time range and returns its equivalent in 24-hour format, raising ValueError on invalid input.


import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matched := re.search(
        r"^(\d\d?):?(\d?\d)? (AM|PM) to (\d\d?):?(\d?\d)? (AM|PM)$",
        s,
    ):

        hours1, minutes1 = parse_time(
            matched.group(1), matched.group(2), matched.group(3)
        )
        hours2, minutes2 = parse_time(
            matched.group(4), matched.group(5), matched.group(6)
        )

        return f"{hours1:02}:{minutes1:02} to {hours2:02}:{minutes2:02}"
    else:
        raise ValueError()


def parse_time(hour, minute, period):
    hour = int(hour)
    minute = int(minute) if minute else 0

    if not (1 <= hour <= 12) or not (0 <= minute <= 59):
        raise ValueError()

    if period == "PM" and hour != 12:
        hour += 12
    elif period == "AM" and hour == 12:
        hour = 0

    return hour, minute


if __name__ == "__main__":
    main()
