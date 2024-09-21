import sys

def main():
    plate = input("Plate: ")
    if not plate[0].isalpha():
        print("Invalid")
        sys.exit(1)

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    z = 0
    b = 0
    c = 0
    d = 0

    if not s[0].isalpha():
        print("Invalid")
        return False

    if len(s) >= 2 and len(s) <= 6:
        if (s[-2]) == "0":
            return False
        elif len(s) >= 2 and len(s) <= 6:
            n = 0
            while n < len(s):
                if s[n].isdigit() == True:
                    c = False
                    if s[-1].isdigit()== True:
                        z = True
                    else:
                        z = False
                elif s[n] == ".":
                    d = True
                else:
                    b = True
                n = n + 1
            if z == True:
                if d == True:
                    return False
                elif (s[-2]).isdigit() == False:
                        return False
                        b = False
                else :
                    return True
                    b = False
            else:
                X = True
            if b == True and c == True:
                return True
            if z == False and b == True:
                return True

        else:
            return False
    else:
        return False

if __name__ == "__main__":
    main()
