import sys
from pyfiglet import Figlet

totalArg = len(sys.argv) - 1

if totalArg == 0:
    userText = input("Input: ")
    figlet = Figlet()
    print(figlet.renderText(userText))
elif totalArg == 2:
    flag = sys.argv[1]
    userFont = sys.argv[2]

    if flag != "-f":
        print("Invalid usage")
        sys.exit(1)
    else:
        figlet = Figlet(font=userFont)
        userText = input("Input: ")
        print(figlet.renderText(userText))
else:
    print("Invalid usage")
    sys.exit(1)
