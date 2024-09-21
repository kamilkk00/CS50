def main ():
    word = str(input("Input: "))
    result = shorten(word)
    print(f"output: {result}")
def shorten (word):
    shorten = word.replace("a", "").replace("A", "").replace("E","").replace("e", "").replace("I","").replace("i", "").replace("O", "").replace("o","").replace("U", "").replace("u","")
    return shorten
if __name__ == "__main__":
    main()
