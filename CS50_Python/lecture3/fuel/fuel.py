while True:
    try:
        x = str(input("x: "))
        y = x.split(sep=".")
        x = x.split(sep="/")
        a = float (x[0])
        b = float (x[1])
    except ValueError:
        z = 0
    else:
        if len(y) > 1:
            z = 0
        else:
            try:
                c = a / b * 100
            except ZeroDivisionError:
                z = 0
            else:
                if c <= 100:
                    if c <= 1:
                        print ("E")
                        break
                    elif c >= 99:
                        print("F")
                        break
                    else:
                        print(f"{c:.0f}%")
                        break
                else:
                    x = str(input("x: "))
