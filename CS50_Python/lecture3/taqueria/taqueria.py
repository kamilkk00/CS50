menu = {
    "baja taco": 4.25,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}
z = True
x = 0
try:
    while z == True:
        order = str(input("Item: ")).lower()
        for cena in menu:
            if order == cena:
                y = menu[cena]
                x = x + y
                print (f"Total: ${x:.2f}")
                z = True
            elif order == "":
                z = False
except EOFError:
    print()
    for key in menu:
        print(menu[key], key)
