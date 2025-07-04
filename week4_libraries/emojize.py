# Emojize — Converts emoji codes or aliases in user input into actual emoji using the emoji module.

import emoji

emo = input("Input: ")

print(emoji.emojize(emo, language='alias'))