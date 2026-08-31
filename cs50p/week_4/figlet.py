import sys
import random
from pyfiglet import Figlet


def main():
    figlet = Figlet()
    fonts = figlet.getFonts()

    if len(sys.argv) == 1:
        randChoice = random.choice(fonts)
        figlet.setFont(font=randChoice)
    elif len(sys.argv) == 3:
        if (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in fonts:
            figlet.setFont(font=sys.argv[2])
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

    text = input("Input: ")
    print(figlet.renderText(text))
   
# # wyciagnac na koncie powtarzajacy sie kod
    
#     print(sys.argv[0])
#     print(sys.argv[1])
#     print(sys.argv[2])
#     print(fonts[1])

main()