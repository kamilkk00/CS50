while True:
    try:
        a = int(input("Height: "))
        if a > 0 and a < 9:
            break
    except ValueError:
        True
c = a - 1
d = 1
for _ in range(a):
    print(" " * c, end="")
    print("#" * d)
    c = c - 1
    d = d + 1
