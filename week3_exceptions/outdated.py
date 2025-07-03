# Outdated — Converts dates from month-day-year format to ISO 8601 (YYYY-MM-DD).

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ").strip()
    if "," in date:
        mmdd, year = date.split(", ")
        month, day = mmdd.split()
        if month.title() in months:
            month = months.index(month)+1

    elif "/" in date:
        month, day, year = date.split("/")

    else: 
        continue
    
    day = int(day)
    month = int(month)
    if day > 31 or month > 12:
        continue

    print(f"{year}-{int(month):02}-{int(day):02}")
    break