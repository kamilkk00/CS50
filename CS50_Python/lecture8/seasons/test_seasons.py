from seasons import date_transformation, counting, into_word
from datetime import date
#tested in 12.09.2023 zawsze można date zmienić
# 5.06.2024

def main():
    test_datetransformation()
    test_counting()
def test_datetransformation():
    assert date_transformation("2022-09-11") == date(2022, 9, 11)
    assert date_transformation("2000-04-19") == date(2000, 4, 19)
def test_counting():
    assert counting("2022-09-11") == 911520
    assert counting("2000-04-19") == 12690720
def test_intoword():
    assert into_word("2022-09-11") == "Nine hundred eleven thousand, five hundred twenty"
    assert into_word("2000-04-19") == "Twelve million, six hundred ninety thousand, seven hundred twenty"

if __name__ == "__main__":
    main()
