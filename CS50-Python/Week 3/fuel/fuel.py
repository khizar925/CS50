def main():
    while True:
        try:
            # Prompt the user for input
            prompt = input("Fraction: ")
            prompt = prompt.split("/")
            numerator = int(prompt[0])
            denominator = int(prompt[1])
            result = numerator / denominator
            result *= 100
            result = int(round(result))

            # Conditions
            if result <= 1:
                print ("E")
                break
            elif result >= 99 and result <= 100:
                print ("F")
                break
            elif result > 100:
                main()
            else:
                print (f"{result}%")
                break
        except (ZeroDivisionError, ValueError):
            pass

main()
