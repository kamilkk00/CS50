import re
import sys

def main():
    sys.exit(print(parse(input("HTML: "))))

def parse(s):
    x = s
    y = re.search(r'.+youtube\.com/embed/(.+)".+', x)
    if y:
        o = y.group(1).split('"')
        a = str(o[0])
        z = ("https://youtu.be/" + a)
        return z
    else:
        return None
if __name__ == "__main__":
    main()
