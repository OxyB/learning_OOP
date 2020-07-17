def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n


class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom


def __str__(self):
    return str(self.num) + "/" + str(self.den)


def show(self):
    print(self.num, "/", self.den)


def __mul__(self, otherfraction):
    new_num = self.num * otherfraction.num
    new_den = self.den * otherfraction.den
    common = gcd(new_num, new_den)
    return Fraction(new_num // common, new_den // common)


x = Fraction(1, 2)
y = Fraction(2, 3)

print("Multiplication")
print(x * y)
