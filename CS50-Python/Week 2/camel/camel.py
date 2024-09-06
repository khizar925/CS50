prompt = input ("camelCase: ")
new_prompt = ""
for char in prompt:
    if char.isupper():
        new_char = char.lower()
        new_prompt = new_prompt + "_" + new_char
    else:
        new_prompt = new_prompt + char

print (f"snake_case: {new_prompt}")
