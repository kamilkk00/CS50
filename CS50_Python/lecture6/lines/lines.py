import sys


try:
    file = sys.argv[1]
except IndexError:
    sys.exit ("Too few command-line arguments")

x = len(sys.argv)
if len(sys.argv) > 2:
    sys.exit ("Too many command-line arguments")
else:
    if (file[-3:]) == ".py":
        try:
            with open (f"{file}", "r") as file:
                cnt = 0
                for line in file:
                    line = line.replace(" ", "")
                    if line[0] == "#":
                        cnt += 0
                    elif len (line) <= 1:
                        cnt += 0
                    elif line[0] == '"""':
                        cnt += 0
                    else:
                        cnt += 1
            print (cnt)
        except FileNotFoundError:
            sys.exit ("File does not exist")

    else:
        sys.exit ("Not a Python file")

