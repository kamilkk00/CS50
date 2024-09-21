one = input("Greeting: ").lower()
wszystkie = one.split()
pierwsze = wszystkie[0]
if pierwsze == "hello" or pierwsze == "hello,":
    print("$0")
elif len(one) > 0:
    firstChar = one[0]
    if firstChar == "h":
        print(f"$20")
    else:
        print("$100")

