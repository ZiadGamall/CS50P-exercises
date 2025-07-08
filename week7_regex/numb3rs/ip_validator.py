# IP validator - Validates whether a given string is a properly formatted IPv4 address.

import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    octet = r"(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)"
    return bool(re.match(fr"^{octet}\.{octet}\.{octet}\.{octet}$", ip))
    
    

if __name__ == "__main__":
    main()