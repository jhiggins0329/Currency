from currency import Currency

def test_two_currencies():
    a = Currency('USD', 8)
    b = Currency('USD', 8)
    assert a == b

def test_two_currecies_false():
    a = Currency('USD', 8)
    b = Currency('USD', 6)
    assert a != b

def test_two_currencies_add():
    a = Currency('USD', 4)
    b = Currency('USD', 5)
    assert a + b == Currency('USD', 9)

# def test_two_currencies_subtract():
#     a = Currency('USD', 5)
#     b = Currency('USD', 3)
#     assert a - b == 2
