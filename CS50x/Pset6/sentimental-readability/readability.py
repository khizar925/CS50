text = input("Text: ")

count = 0
s = 0
letters = 0
for i in text:
    if i == "." or i == "?" or i == "!":
        s += 1
    if i.isalpha():
        letters += 1

size = len(text)
words = len(text.split())


letters_per_100_words = (letters / words) * 100

sentences_per_100_words = (s / words) * 100

index = 0.0588 * letters_per_100_words - 0.296 * sentences_per_100_words - 15.8
index = int(round(index))

if index < 1:
    print("Before Grade 1")
elif index >= 16:
    print("Grade 16+")
else:
    print(f"Grade {index}")
