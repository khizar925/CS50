def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    d = d.replace("$", "")
    d1 = float(d)
    return d1


def percent_to_float(p):
    # TODO
    p = p.replace("%", "")
    d2 = float(p)
    return d2 / 100


main()
