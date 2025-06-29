# Meal Time — Determines whether the time is breakfast, lunch, or dinner based on user input.

def main():
    timeParts = input("Enter the time: ").strip().lower().split()
    hours, minutes = timeParts[0].split(":")
    
    if len(timeParts) == 2:
        time = Convert24Hr(hours, minutes, timeParts[-1])
    else:
        time = Convert24Hr(hours, minutes)

    if 7 <= time <= 8:
        print("Breakfast time")
    elif 12 <= time <= 13:
        print("Lunch time")
    elif 18 <= time <= 19:
        print("Dinner time")
    else:
        print("It's not the time to eat yet")


def Convert24Hr(hour, minute, period=None):
    hour = int(hour)
    minute = int(minute)
    if period:
        if "p" in period.lower() and hour != 12:
            hour += 12
        elif "a" in period.lower() and hour == 12:
            hour = 0
    return hour + minute / 60

main()