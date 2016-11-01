from currency import Currency
# Must equal another Currency object with the same amount and currency code.
def test_two_currencies():
    a = Currency('USD', 8)
    b = Currency('USD', 8)
    assert a == b
# Must NOT equal another Currency object with different amount or currency code.
def test_two_currecies_false():
    a = Currency('USD', 8)
    b = Currency('USD', 6)
    assert a != b
# Must be able to be added to another Currency object with the same currency code.
def test_two_currencies_add():
    a = Currency('USD', 4)
    b = Currency('USD', 5)
    assert a + b == Currency('USD', 9)
# Must be able to be subtracted by another Currency object with the same currency code.
def test_two_currencies_subtract():
    a = Currency('USD', 6)
    b = Currency('USD', 6)
    assert a - b == Currency('USD', 0)
# Must raise a DifferentCurrencyCodeError when you try to add or subtract two Currency objects with different currency codes.


# Must be able to be multiplied by an int or float and return a Currency object.
def test_two_currencies_multiply():
    a = Currency('USD', 6)
    b = Currency('USD', 6)
    assert a * b == ('USD', 36)

        # curr1 = Currency(100, 'USD')
        # enter_number = 9
        #
        # assert  curr1 * enter_number == (900, 'USD')
# def test_two_currencies_subtract():
#     a = Currency('USD', 5)
#     b = Currency('USD', 3)
#     assert a - b == 2
