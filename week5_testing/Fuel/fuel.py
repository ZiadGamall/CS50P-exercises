# Fuel Gauge — Prompts for a fraction and displays the fuel level as a percentage or as E/F for empty/full.


def main():
    while True:
        try:
            result = convert(input("Fraction: "))
            print(result)
            break
        except (ValueError, ZeroDivisionError):
            continue


def convert(fraction: str) -> str:
    numText, denoText = fraction.strip().split("/")
    if "." in numText or "." in denoText:
        raise ValueError
    numerator = int(numText)
    denominator = int(denoText)
    if denominator == 0:
        raise ZeroDivisionError
    percent = int((numerator / denominator) * 100)
    if percent > 100:
        raise ValueError
    if percent <= 1:
        return "E"
    elif percent == 100:
        return "F"
    else:
        return f"{percent}%"


if __name__ == "__main__":
    main()
