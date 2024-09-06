prompt = input ("Greeting: ")

prompt = prompt.lower().strip()
if prompt.find("hello") == 0:
    print ("$0")
elif prompt[0] == 'h':
    print ("$20")
else:
    print ("$100")
