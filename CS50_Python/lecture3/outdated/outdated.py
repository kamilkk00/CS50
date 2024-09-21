z = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
months = {
    "January" : 1,
    "February": 2,
    "March" : 3,
    "April" : 4,
    "May" : 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

while True:
    date = str (input("Date: "))
    if date[0] == " ":
        date == date[1:]
    if date [-5] == "/":
        try:
            a = date.split("/")
            al0 = "".join([(element) for element in a[0]])
            a0 = int(al0)
            if a0 < 13:
                al1 = "".join([(element) for element in a[1]])
                a1 = int(al1)
                if a1 < 32 and a1 > 0:
                    b = True
                    break
        except ValueError:
            p = 0
    else:
        try:
            zo = date.replace(","," , ").split(" ")
            if zo[2] == ",":
                a = date.replace(",", "").split(" ")
                al1 = "".join([(element) for element in a[1]])
                a1 = int(al1)
                if a1 < 32:
                    try:
                        z.index(a[0])
                        b = False
                        break
                    except ValueError:
                        p = 0
        except ValueError:
            p = 0


if b == True:
    print (f"{a[2]}-{a0:02}-{a1:02}")
else:
    b = months[a[0]]
    print (f"{a[2]}-{b:02}-{a1:02}")
