# Deep Thought — Responds "Yes" if user enters 42, forty-two, or forty two; otherwise responds "No".

answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

# if answer == "42" or answer.lower() == "forty two" or answer.lower() == "forty-two":
#     print("Yes")
# else :
#     print("no")

print ("yes") if answer == "42" or answer.lower() == "forty two" or answer.lower() == "forty-two" else print("no")