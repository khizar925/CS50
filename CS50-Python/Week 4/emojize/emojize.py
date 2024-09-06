import emoji

userInput = input("Input: ")

output = emoji.emojize(userInput, language='alias')

print(f"Output: {output}")
