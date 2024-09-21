from twttr import shorten

def main():
    test_shorten()
    test_shorten2()
def test_shorten():
    assert shorten ("Twitter") == "Twttr"
    assert shorten ("What's your name?") == "Wht's yr nm?"
    assert shorten ("CS50") == "CS50"
def test_shorten2():
    assert shorten ("twitter") == "twttr"
    assert shorten ("Anna") == "nn"
if __name__ == "__main__":
    main()
