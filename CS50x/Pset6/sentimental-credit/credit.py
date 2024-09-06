def main():
    number = input("Number: ")
    size = len(number)

    if checkSum(number):
        if size == 15 and (number[:2] == "34" or number[:2] == "37"):
            print("AMEX")
        elif (size == 13 or size == 16) and number[:1] == "4":
            print("VISA")
        elif size == 16 and "51" <= number[:2] <= "55":
            print("MASTERCARD")
        else:
            print("INVALID")
    else:
        print("INVALID")


def checkSum(number):
    digits = [int(digit) for digit in number[::-1]]  # Reverse the digits for easier processing
    total_sum = 0

    for i in range(1, len(digits), 2):
        double_digit = digits[i] * 2
        total_sum += double_digit if double_digit < 10 else double_digit - 9

    total_sum += sum(digits[0::2])

    return total_sum % 10 == 0


main()
