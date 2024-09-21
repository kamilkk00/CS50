import re

def main():
    print(count(input("Text: ")))
def count(s):
    a = s.replace(",", "").replace("?", "").replace(".", "").split(" ")
    z = 0
    p = 0
    while p <= len(a):
        try:
            if matches := re.search(r"^um$", a[p], re.IGNORECASE):
                p = p + 1
                z = z + 1
            else:
                p = p + 1
        except IndexError:
            z = z
            p = p + 1
    return z

if __name__ == "__main__":
    main()
