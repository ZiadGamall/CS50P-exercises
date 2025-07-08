# Email validator - Prompts the user for an email address and prints Valid or Invalid based on its syntax using validator-collection.

from validator_collection import validators, errors


email = input("What's your email? ")
try:
    validators.email(email)
    print("Valid")

except errors.InvalidEmailError:
    print("Invalid")
