from bank import value

def main():
    test_value0()
    test_value1()
    test_upper()

def test_value0():
    assert value ("hello") == 0
    assert value ("hello, Newman") == 0

def test_value1():
    assert value ("how you doing?") == 20
    assert value ("What's happening") == 100

def test_upper():
    assert value ("HI") == 20

if __name__ == "__main__":
    main()


