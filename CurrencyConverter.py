from currency import Currency

class CurrencyConverter:

    conversion_rates = {'USD': 1.0, 'EUR': 0.74, 'JPY': 120.0}

    def __init__(self, rates):
        self.rates = rates
# Must raise an UnknownCurrencyCodeError when you try to convert from or to a currency code it doesn't know about.
class UnknownCurrencyCodeError(Exception):
    pass
