def main():
    prompt = input("Input: ")
    new_prompt = ""
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for char in prompt:
        if char in vowels:
            pass
        else:
            new_prompt = new_prompt + char
    print (f"Output: {new_prompt}")

main()
