from numb3rs import validate
import re

def main():
    test_validate1()
    test_validate2()
    test_invalid1()
    test_invalid2()
    test_invalid3()
    test_0()
    test_range()
def test_range():
    assert validate(r"1.512.1.1")==False
def test_0():
    assert validate(r"1.2.3.4")==True
    assert validate(r"1.2.3")==False
    assert validate(r"1.2")==False
    assert validate(r"1")==False
def test_validate1():
    assert validate (r"127.0.0.1") == True
def test_validate2():
    assert validate (r"255.255.255.255") == True
def test_invalid1():
    assert validate (r"512.512.512.512") == False
def test_invalid2():
    assert validate (r"cat") == False
def test_invalid3():
    assert validate (r"1.2000.3.1") == False
def test_nie():
    assert validate (r"10.10.10.10.10") == False

if __name__ == "__main__":
    main()

