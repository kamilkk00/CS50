def main ():
    greeting = input("Greeting: ")
    print(f"${value(greeting)}")

def value (greeting):
    greeting = greeting.lower()
    wszystkie = greeting.split()
    pierwsze = wszystkie[0]
    if pierwsze == "hello" or pierwsze == "hello,":
        return 0
    elif len(greeting) > 0:
        firstChar = greeting[0]
        if firstChar == "h":
            return 20
        else:
            return 100

if __name__ == "__main__":
    main()



