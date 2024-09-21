from um import count

def main():
    test_um1()
    test_um2()
    test_um_upper()
    test_um_dot()
def test_um1():
    assert count("um") == 1
def test_um2():
    assert count ("Um, thanks, um...") == 2
def test_um_upper():
    assert count ("Um, thanks for the album.") == 1
def test_um_dot():
    assert count ("Um..... um heh ") == 2


if __name__ == "__main__":
    main()
