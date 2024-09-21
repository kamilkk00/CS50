from plates import is_valid

def main():
    test_valid()
    test_invalid()
    test_invalid_dots()
    test_valid_one_letter()
    test_invalid_uppercase()
    test_invalid_last()
    test_valid_alphabetic()
    test_valid_alhpa()
def test_valid():
    assert is_valid ("CS50") == True
def test_invalid():
    assert is_valid ("CS05") == False
def test_invalid_dots():
    assert is_valid ("PI3.14") == False
def test_valid_one_letter():
    assert is_valid ("H") == False
def test_invalid_uppercase():
    assert is_valid ("OUTATIME") == False
def test_invalid_last():
    assert is_valid ("CS50P2") == False
def test_valid_alphabetic():
    assert is_valid ("NRVOUS") == True
def test_valid_alhpa():
    assert is_valid ("abc") == True
    assert is_valid ("22") == False
if __name__ == "__main__":
    main()
