def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    n = len(s)
    if n < 2 or n > 6:
        return False

    if not s[0].isalpha() or not s[1].isalpha():
        return False

    i = 0
    for ch in s:
        if not ch.isalpha() and not ch.isdigit():
            return False
        if ch.isdigit():
            break
        i += 1

    if i == 6:
        return True
    else:
        s2 = s[i:]
        if s2[0] == '0':
            return False
        for ch in s2:
            if not ch.isalpha() and not ch.isdigit():
                return False
            if ch.isalpha():
                return False
    return True


main()
