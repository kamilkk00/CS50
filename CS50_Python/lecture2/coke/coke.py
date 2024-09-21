print ("Amount Due: 50")
z = int(input("Insert Coin: "))
x = 50
while x > 0:
    if z == 25 or z == 10 or z == 5:
         x = 50 - z
         while x > 0:
                print (f"Amount Due: {x}")
                coin2 = int(input("Insert Coin: "))
                x = x - coin2
                if x == 0:
                    print("Change Owed: 0")
                    break
                if x < 0:
                     print(f"Change Owed: {-x}")
    elif z != 25 or z != 10 or z != 5:
        x = x
        print (f"Amount Due: {x}")
        z = int(input("Insert Coin: "))
