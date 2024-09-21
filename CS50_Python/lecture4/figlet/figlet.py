import sys
from pyfiglet import Figlet
from pyfiglet import figlet_format

figlet = Figlet()
a = figlet.getFonts()
try:
    a.index(sys.argv[2])
    if sys.argv[1] == "-f" or sys.argv[1] =="--font":
        try:
            b = figlet.setFont(font=sys.argv[2])
            x = str(input("Input: "))
            result = figlet.renderText(f"{x}")
            print (result)
        except IndexError:
            p = 0
            print ("Invalid usage")
            sys.exit(1)
    else:
        print ("Invalid usage")
        sys.exit(1)
except ValueError:
    print ("Invalid usage")
    sys.exit(1)

