def main():
    prompt = input ("Input : ")
    new_prompt = convert(prompt)
    print (new_prompt)

def convert(prompt):
    new_prompt = prompt.replace (":)" , "🙂")
    new_prompt = new_prompt.replace (":(" , "🙁")
    return new_prompt

main()
