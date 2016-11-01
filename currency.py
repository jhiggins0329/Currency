class Currency:
# Must be created with an amount and a currency code.
    def __init__(self, currency_code, value):
        self.value = value
        self.currency_code = currency_code
        pass

    def __eq__(self, other):
        if self.currency_code == other.currency_code and self.value == other.value:
            return True
        return False

    def __add__(self, value):
        return '{} plus {}'.format(self.value, value)
        if self.currency_code == other.currency_code
        pass

    def __sub__(self, other):
        if self.currency_code == other.currency_code and self.value == other.value:
            return Currency()
        pass
    def __ne__(self, other):
        return not self.__eq__(other)

    def __mul__(self, other):
        return Currency * Currency

# def __add__(self, other):
#     if self.value + other.value == Currency
#         return Currency(self.currency_code, self.value + other.value)
#     else:
#         pass
#     def (arg):
#         pass __add__(self, other):
#         if self.value == other.value
#             return Currency


# Currency() must be able to take one argument with a currency symbol embedded in it, like "$1.20" or "€ 7.00", and figure out the correct currency code. It can also take two arguments, one being the amount and the other being the currency code.
