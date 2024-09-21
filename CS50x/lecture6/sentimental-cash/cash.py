while True:
    a = 0
    while True:
        try:
            b = float(input("Change owed: "))
            break
        except ValueError:
            True
    i = b * 100
    if i > 0:
        while i >= 25:
            a = a + 1
            i = i - 25
        while i >= 10:
            a = a + 1
            i = i - 10
        while i >= 5:
            a = a + 1
            i = i - 5
        while i >= 1:
            a = a + 1
            i = i - 5
        print(a)
        break
