# Adieu — Prompts for names and bids farewell in grammatically correct Oxford comma format.

names = []

while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        break

print ("Adeiu, adieu, to ", end="")

if len(names) == 1:
    print(names[0])

elif len(names) == 2:
    print(f"{names[0]} and {names[1]}")

else:
    print(f"{', '.join(names[:-1])}, and {names[-1]}")