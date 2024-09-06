def main():
    amount = int(50)
    sum = 0
    while amount > 0:
        print (f"Amount Due: {amount}")
        prompt = int(input("Insert Coin: "))
        if prompt == 25 or prompt == 10 or prompt == 5:
            amount = amount - prompt
            sum = sum + prompt
        if sum >= 50:
            print (f"Change Owed: {abs(amount)}")
            break

main()
