"""Implement a class Money to represent value and currency.
You need to implement methods to use all basic arithmetics expressions
(comparison, division, multiplication, addition and subtraction).
Tip: use class attribute exchange rate which is dictionary and
stores information about exchange rates to your default currency.
Have a look at @functools.total_ordering
"""

exchange_rate = {
    "EUR": 0.86,
    "BYN": 2.5,
    "USD": 1,
    "JPY": 111.33
}

class Money:

    def __init__(self, value: (int, float), currency="USD"):
        self.value = value
        self.currency = currency
        self.rate = exchange_rate[currency]


    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Money(self.value + other, self.currency)
        elif isinstance(other, Money):
            unit = self.rate / other.rate
            return Money(self.value + (other.value * unit), self.currency)


    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return Money(self.value - other, self.currency)
        elif isinstance(other, Money):
            unit = self.rate / other.rate
            return Money(self.value - (other.value * unit), self.currency)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Money(self.value * other, self.currency)
        elif isinstance(other, Money):
            unit = self.rate / other.rate
            return Money(self.value * (other.value * unit), self.currency)

    def __div__(self, other):
        if isinstance(other, (int, float)):
            return Money(self.value / other, self.currency)
        elif isinstance(other, Money):
            unit = self.rate / other.rate
            return Money(self.value / (other.value * unit), self.currency)

    def __radd__(self, other):
        if isinstance(other, (int, float)):
            return Money(other + self.value, self.currency)
        elif isinstance(other, Money):
            unit = self.rate / other.rate
            return Money((other.value * unit) + self.value, self.currency)

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            return Money(other - self.value, self.currency)
        elif isinstance(other, Money):
            unit = self.rate / other.rate
            return Money((other.value * unit) - self.value, self.currency)

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return Money(other * self.value, self.currency)
        elif isinstance(other, Money):
            unit = self.rate / other.rate
            return Money((other.value * unit) * self.value, self.currency)

    def __rdiv__(self, other):
        if isinstance(other, (int, float)):
            return Money(other / self.value, self.currency)
        elif isinstance(other, Money):
            unit = self.rate / other.rate
            return Money((other.value * unit) / self.value, self.currency)

    def __lt__(self, other):
        if isinstance(other, (int, float)):
            return self.value < other
        elif isinstance(other, Money):
            unit = self.rate / other.rate
            return self.value < (other.value * unit)

    def __gt__(self, other):
        if isinstance(other, (int, float)):
            return self.value > other
        elif isinstance(other, Money):
            unit = self.rate / other.rate
            return self.value > (other.value * unit)

    def __le__(self, other):
        if isinstance(other, (int, float)):
            return self.value <= other
        elif isinstance(other, Money):
            unit = self.rate / other.rate
            return self.value <= (other.value * unit)

    def __ge__(self, other):
        if isinstance(other, (int, float)):
            return self.value >= other
        elif isinstance(other, Money):
            unit = self.rate / other.rate
            return self.value >= (other.value * unit)

    def __eq__(self, other):
        if isinstance(other, (int, float)):
            return self.value == other
        elif isinstance(other, Money):
            unit = self.rate / other.rate
            return self.value == (other.value * unit)

    def __ne__(self, other):
        if isinstance(other, (int, float)):
            return self.value != other
        elif isinstance(other, Money):
            unit = self.rate / other.rate
            return self.value != (other.value * unit)

    def __repr__(self):
        return f"{self.value:.2f} {self.currency}"

x = Money(10, "BYN")
y = Money(11)
print("x + y:", x+y)
z = Money(12.34, "EUR")
print("z + 3.11 * x + y * 0.8:", z + 3.11 * x + y * 0.8) # result in “EUR”
#  12.34 +   10.698 +  7,568  = 30.61

lst = [Money(10, "BYN"), Money(11), Money(12.01, "JPY")]
s = sum(lst)
print(s) #result in “BYN”
