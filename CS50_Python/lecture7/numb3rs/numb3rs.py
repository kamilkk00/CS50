import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    x = ip
    try:
        y = re.search(r'^(?:([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+))$', x)
        if y:
            z1 = int (y.group (1))
            z2 = int (y.group (2))
            z3 = int (y.group (3))
            z4 = int (y.group (4))
            if z1 < 256 and z2 < 256 and z3 < 256 and z4 < 256:
                return True
            else:
                return False
    except re.error:
        return False
    else:
        return False


if __name__ == "__main__":
    main()
