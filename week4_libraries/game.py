# Number Guessing Game — Randomly picks a number and prompts user to guess it with feedback.

import random

while True:
    limit = input("level: ")
    try:
        limit = int(limit)
    except ValueError:
        continue

    if limit > 0:
        break

num = random.randint(1, limit)

while True:
    guess = input("Guess: ")
    try:
        guess = int(guess)
        if guess <= 0:
            raise ValueError
    except ValueError:
        continue

    if guess < num:
        print("Too small!")
    elif guess > num:
        print("Too large!")
    else:
        print("Just right!")
        break
