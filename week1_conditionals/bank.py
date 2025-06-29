# Bank — Analyzes user greeting to determine a cash reward based on how the greeting starts.

greeting = input("Greeting: ").lower().strip()

if(greeting.startswith("hello")):
    print("$0")
elif(greeting.startswith("h")):
    print("$20")
else:
    print("$100")