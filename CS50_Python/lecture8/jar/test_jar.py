from jar import Jar

def main():
    test_str()

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
def test_deposit():
    assert Jar().deposit(1) == None
def test_withdraw():
    assert Jar(10).size == 0
def test_capacity():
    assert Jar(5).capacity == 5


if __name__ == "__main__":
    main()
