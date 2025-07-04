# Little Professor — Simulates a math quiz toy with random addition problems and limited attempts.

import random

def main():
    score = 0
    level = get_level()
    for i in range(10):
        num1 = generate_integer(level)
        num2 = generate_integer(level)
        solution = num1 + num2



        for i in range(3):
            try:
                answer = int(input(f"{num1} + {num2} = "))
                if answer == solution:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
                
        else:
            print(f"{num1} + {num2} = {num1 + num2}")
                    
    
    print(f"Score: {score}")


        


def get_level():
    while True:
        level = input("Level: ")
        try:
            level = int(level)
            if 3 < level or level < 1:
                raise ValueError
            else:
                return level
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    else:
        return random.randint(100,999)


if __name__ == "__main__":
    main()