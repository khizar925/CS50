from cs50 import get_int

while True:
    height = get_int("Height: ")
    if height >= 1 and height <= 8:
        break

for i in range(height):
    spaces = height - i - 1
    hashes = i + 1

    print(" " * spaces, end="")
    print("#" * hashes, end="")
    print()
