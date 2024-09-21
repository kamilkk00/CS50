from project import rating, maturity, total_cost

def main():
    test_interest()
    test_maturity()
    test_total_cost()

def test_interest():
    assert rating("AA") == 1.5
    assert rating("B") == 8
    assert rating("CCC") == 12

def test_maturity():
    assert maturity(3) == 1
    assert maturity(15) == 3
    assert maturity(80) == 4

def test_total_cost():
    assert total_cost(1000, 10, 1) == 100
    assert total_cost(5000, 5, 3) == 750
    assert total_cost(25000, 8, 10) == 20000

if __name__ == "__main__":
    main()
