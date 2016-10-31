class Currency:
    def __init__(self, currency_code, value):
        self.value = value
        self.currency_code = currency_code
        pass

    def __eq__(self, other):
        if self.currency_code == other.currency_code and self.value == other.value:
            return True
        return False

    def __add__(self, other):
        if self.value == other.value:
            return Currency

#     def (arg):
#         pass __add__(self, other):
#         if self.value == other.value
#             return Currency
#
#     def hg
