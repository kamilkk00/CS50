from fuel import convert, gauge
import pytest

def main():
    test_convert()
    test_convert1()
    test_convert2()
    test_gauge()
    test_convert_exceptions()

def test_convert():
    assert convert("1/4") == 25.0

def test_convert1():
    assert convert("1/2") == 50.0

def test_convert2():
    assert convert("1/1") == 100.0

def test_gauge():
    assert gauge(99) == "F"
    assert gauge(50) == "50%"
    assert gauge(1) == "E"

def test_convert_exceptions():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("invalid")
    with pytest.raises(ValueError):
        convert("1.0/2")



if __name__ == "__main__":
    main()
