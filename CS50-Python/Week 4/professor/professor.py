import random

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y

        # Allow the user up to 3 attempts to get the correct answer
        for attempt in range(3):
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == correct_answer:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
        else:
            print(f"{x} + {y} = {correct_answer}")

    # Output only the score as an integer
    print(score)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass
        print("Please enter a valid level (1, 2, or 3).")

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)  # Single digit
    elif level == 2:
        return random.randint(10, 99)  # Two digits
    elif level == 3:
        return random.randint(100, 999)  # Three digits
    else:
        raise ValueError("Level must be 1, 2, or 3.")

if __name__ == "__main__":
    main()
