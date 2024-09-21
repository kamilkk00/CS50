from working import convert
import pytest

def main():
    test_valid1()
    test_valid2()
    test_valid3()
    test_invalid()
    test_valueerror()
    test_invalid_minutes()

def test_valid1():
    assert convert("9 AM to 5 PM") == ("09:00 to 17:00")
def test_valid2():
    assert convert("9:00 AM to 5:00 PM") == ('09:00 to 17:00')
def test_valid3():
    assert convert("8 PM to 8 AM") == ('20:00 to 08:00')
def test_invalid():
    with pytest.raises(ValueError):
        convert("10:7 AM - 5:1 PM")
def test_valueerror():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
def test_invalid_minutes():
    with pytest.raises(ValueError):
        convert("8:60 AM to 4:60 PM")


if __name__ == "__main__":
    main()
