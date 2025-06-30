# Vanity Plates — Validates a custom license plate string based on specific formatting rules.

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
    
def is_valid(s):

    # Length check
    if not (2 <= len(s) <=6):
        return False

    # Symbol and puctuation marks check
    for letter in s:
        if not letter.isalnum():
            return False
    
    # First 2 characters are letters check
    if not (s[0].isalpha() and s[1].isalpha()):
        return False
    
    # Storing the numbers
    numbers = ""
    for i in range(len(s)):
        if s[i].isdigit():
            numbers = s[i:]
            break
    
    # Numbers starting with 0 checl
    if numbers and numbers[0] == "0":
        return False

    # Letter after the numbers check
    if not numbers.isdigit():
        return False
    

    return True

main()