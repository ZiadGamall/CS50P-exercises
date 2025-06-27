# Making faces - Convert :) and :( to emojis

def convert(text):
    text = text.replace(":)","🙂").replace(":(","🙁")
    return text

def main ():
    text = input("Enter a string: ")
    newText = convert(text)
    print(newText)


main()
